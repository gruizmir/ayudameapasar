# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from ayudantias.models import Ayudantia, AlumnoAyudantia, HorarioAyudantia
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core import mail
from django.core.context_processors import csrf
from django.core.exceptions import ObjectDoesNotExist, PermissionDenied, SuspiciousOperation
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.utils import simplejson
from evaluaciones.models import ReporteAbusoAlumno, ReporteAbusoAyudante
from main.models import Institucion
from usuarios.models import *
from usuarios.forms import *
import uuid


def loginView(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if 'next' in request.GET:
            redir = request.GET['next']
        else:
            redir=None
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(username=email, password=password)
            if user is not None:
                login(request,user)
                if redir==None:
                    return HttpResponseRedirect("/cuentas/perfil")
                else:
                    return HttpResponseRedirect(redir)
        else:
            return render_to_response("login.html", {'form':form}, context_instance=RequestContext(request))
    else:
        form = LoginForm()
        return render_to_response("login.html", {'form':form}, context_instance=RequestContext(request))


def registerView(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(form.cleaned_data['email'], email=form.cleaned_data['email'], password=form.cleaned_data['password2'])
            user.first_name = form.cleaned_data['nombre']
            user.last_name = form.cleaned_data['apellido']
            user.is_active = False
            user.save()
            perfil = user.perfil
            perfil.institucion = form.cleaned_data['institucion']
            perfil.es_ayudante = False
            perfil.save()
            if user.perfil.es_ayudante:
                ayudante = Ayudante(usuario=user)
                ayudante.save()
            sendConfirmationEmail(user)
            return HttpResponseRedirect("/")
        else:
            return render_to_response("register.html", {'form':form}, context_instance=RequestContext(request))
    else:
        form = RegisterForm()
        return render_to_response("register.html", {'form':form}, context_instance=RequestContext(request))


def logoutView(request):
    logout(request)
    return HttpResponseRedirect("/")


def sendConfirmationEmail(user):
    connection = mail.get_connection()
    connection.open()
    token = uuid.uuid1().hex
    confReg = UsuarioPorConfirmar(usuario=user, token=token)
    confReg.save()
    msg = user.get_full_name() + u", Bienvenido a Ayudame a Pasar!\n\n"
    msg = msg + u"Confirma tu dirección haciendo click en el siguiente link: \n\n"
    msgCustom = msg + settings.WEB_URL + u"/cuentas/confirmar/" + token + "?email=" + user.email
    subject = "Confirma tu registro en AyudameaPasar.cl"
    try:
        email = mail.EmailMessage(subject, msgCustom, settings.EMAIL_HOST_USER, [user.email], connection=connection)
    except:
        return HttpResponseRedirect("/")
    connection.send_messages([email])
    connection.close()
    return True


def confirm(request, token=None):
    if token==None:
        return HttpResponseRedirect("/")
    else:
        if 'email' in request.GET:
            try:
                user = User.objects.get(email=request.GET['email'])
                if user.is_active == False:
                    confirmar = UsuarioPorConfirmar.objects.get(usuario=user)
                    if confirmar.token == token:
                        user.is_active=True
                        user.save()
                    else:
                        raise Http404
                return HttpResponseRedirect("/cuentas/perfil")
            except:
                return HttpResponseRedirect("/cuentas/registro/")
        else:
            raise PermissionDenied

@login_required
def mostrarPerfilPropio(request):
    user = request.user
    data = {}
    user.profile = Perfil.objects.get(usuario = user)
    data['user'] = user
    actual = datetime.now()
    misSolicitudes  = AlumnoAyudantia.objects.filter(aceptada=False).filter(alumno=user).order_by("-id")
    data['solicitudes'] = misSolicitudes
    evaluar_mis_ayudantes = AlumnoAyudantia.objects.filter(alumno=user).filter(fecha_realizacion__lt = actual.date()).filter(alumno_evaluo=False)
    data['evaluaciones_ayudantes'] = evaluar_mis_ayudantes
    data['reportes_alumno'] = ReporteAbusoAlumno.objects.filter(alumno=user).count()
    if user.perfil.es_ayudante:
        try:
            ayudantias = Ayudantia.objects.filter(ayudante=user.ayudante)
            solicitudesPend = AlumnoAyudantia.objects.filter(aceptada=False).filter(ayudantia__in=ayudantias).order_by("-id")
            agenda  = AlumnoAyudantia.objects.filter(aceptada=True).filter(ayudantia__in=ayudantias).filter(fecha_realizacion__gte = actual.date()).order_by("-id")
            evaluar_mis_alumnos = AlumnoAyudantia.objects.filter(ayudantia__in=ayudantias).filter(fecha_realizacion__lt = actual.date()).filter(ayudante_evaluo=False)
            data['solicitudes_pend'] = solicitudesPend
            data['agenda'] = agenda
            data['ayudantias'] = ayudantias
            data['evaluaciones_alumnos'] = evaluar_mis_alumnos
            data['reportes_ayudante'] = ReporteAbusoAyudante.objects.filter(ayudante=user.ayudante).count()
            data['info'] = InfoAcademica.objects.filter(ayudante=user.ayudante)
        except ObjectDoesNotExist:
            pass
    return render_to_response("perfil_alumno.html", data, context_instance=RequestContext(request))

@login_required
def mostrarPerfil(request, idUser):
    user = get_object_or_404(User, pk=idUser)
    data = {}
    data['user'] = user
    if user.perfil.es_ayudante:
        try:
            data['ayudantias'] = Ayudantia.objects.filter(ayudante=user.ayudante)
            data['info'] = InfoAcademica.objects.filter(ayudante=user.ayudante)
        except ObjectDoesNotExist:
            pass
    return render_to_response("perfil_alumno.html", data, context_instance=RequestContext(request))


@login_required
def edit(request):
    if request.is_ajax():
        form = EditUserForm(request.POST)
        
        if form.is_valid():
            try:
                ub = User.objects.get(email=form.cleaned_data['email'])
                if ub is not request.user:
                    exist=True
                else:
                    exist=False
            except:
                exist=False
                
            user = request.user
            user.first_name = form.cleaned_data['nombre']
            user.last_name = form.cleaned_data['apellido']
            perfil = user.perfil
            perfil.institucion = form.cleaned_data['institucion']
            if form.cleaned_data['institucion'] is not None:
                perfil.avatar = form.cleaned_data['institucion']
            if not exist:
                user.email = form.cleaned_data['email']
            perfil.fono = form.cleaned_data['fono']
            perfil.save()
            user.save()
            data = {}
            data['user'] = user
            rend = render_to_response("seccion_perfil.html", data, context_instance=RequestContext(request))
            message = {"response":"OK", "result": rend.content}
            json = simplejson.dumps(message)
            return HttpResponse(json, mimetype='application/json')
        else:
            data = {}
            data['user'] = request.user
            data['form'] = form
            rend = render_to_response("edit_perfil.html", data, context_instance=RequestContext(request))
            message = {"response":"ERROR", "result": rend.content}
            json = simplejson.dumps(message)
            return HttpResponse(json, mimetype='application/json')
    else:
        raise SuspiciousOperation

@login_required
def getEditForm(request):
    if request.is_ajax():
        user = request.user
        initial_data = {'nombre':user.first_name,
                        'apellido':user.last_name,
                        'institucion':user.perfil.institucion,
                        'avatar':user.perfil.avatar,
                        'email':user.email,
                        'fono':user.perfil.fono
                         }
        data = {}
        data['user'] = request.user
        data['form'] = EditUserForm(initial=initial_data)
        rend = render_to_response("edit_perfil.html", data, context_instance=RequestContext(request))
        message = {"response":"OK", "result": rend.content}
        json = simplejson.dumps(message)
        return HttpResponse(json, mimetype='application/json')
    else:
        raise SuspiciousOperation
