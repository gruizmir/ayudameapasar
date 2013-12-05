# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.context_processors import csrf
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.utils import simplejson
from evaluaciones.models import *
from evaluaciones.forms import *
from usuarios.models import Ayudante
from ayudantias.models import Ayudantia, AlumnoAyudantia


# Se trabaja sobre la base de que las llamadas van a ser por ajax.
# La idea es que sean mini-formularios dentro de dialogos.

def evalAyudantia(request, idAlumnoAyudantia=None):
    if request.is_ajax():
        form = EvalForm(request.POST)
        if form.is_valid():
            try:
                alumnoAyudantia = AlumnoAyudantia.objects.get(id=idAlumnoAyudantia)
                ayudantia = alumnoAyudantia.ayudantia
                punt = PuntuacionAyudantes(ayudantia=ayudantia, puntaje=form.cleaned_data['puntaje'], description=form.cleaned_data['descripcion'])
                punt.save()
                
                ayudante = ayudantia.ayudante
                ayudante.eval_qty = ayudante.eval_qty +1
                ayudante.puntuacion = (ayudante.puntuacion + punt.puntaje)/ayudante.eval_qty
                ayudante.save()
                alumnoAyudantia.alumno_evaluo = True
                alumnoAyudantia.save()
                message = {"response": "OK"}
            except Exception as e:
                print e
                message = {"response": "ERROR", "result":"404"}
        else:
            print form
            message = {"response": "ERROR", "result":"WRONG DATA"}
    else:
        return HttpResponse("ERROR")
    json = simplejson.dumps(message)
    return HttpResponse(json, mimetype='application/json')

def evalAlumno(request, idAlumnoAyudantia=None):
    if request.is_ajax():
        form = EvalForm(request.POST)
        if form.is_valid():
            try:
                alumnoAyudantia = AlumnoAyudantia.objects.get(id=idAlumnoAyudantia)
                alumno = alumnoAyudantia.alumno
                punt = PuntuacionAlumno(usuario=alumno, puntaje=form.cleaned_data['puntaje'], description=form.cleaned_data['descripcion'])
                punt.save()
                perfil = alumno.perfil
                perfil.eval_qty = perfil.eval_qty +1
                perfil.puntuacion = (perfil.puntuacion + punt.puntaje)/perfil.eval_qty
                perfil.save()
                alumnoAyudantia.ayudante_evaluo = True
                alumnoAyudantia.save()
                message = {"response": "OK"}
            except Exception as e:
                print e
                message = {"response": "ERROR", "result":"404"}
        else:
            message = {"response": "ERROR", "result":"WRONG DATA"}
    else:
        return HttpResponse("ERROR")
    json = simplejson.dumps(message)
    return HttpResponse(json, mimetype='application/json')


def abusoAlumno(request, idAlumno=None):
    if request.is_ajax():
        form = AbusoForm(request.POST)
        if form.is_valid():
            try:
                alumno = User.objects.get(id=idAlumno)
                ayudante = request.user.ayudante
                reporte = ReporteAbusoAlumno(alumno=alumno, reportador=ayudante, motivo=form.cleaned_data['motivo'], comentario=form.cleaned_data['comentario'])
                reporte.save()
                message = {"response": "OK"}
            except:
                message = {"response": "ERROR", "result":"404"}
        else:
            message = {"response": "ERROR", "result":"WRONG DATA"}
    else:
        return HttpResponse("ERROR")
    json = simplejson.dumps(message)
    return HttpResponse(json, mimetype='application/json')


def abusoAyudante(request, idAyudante=None):
    if request.is_ajax():
        form = AbusoForm(request.POST)
        if form.is_valid():
            try:
                ayudante = Ayudante.objects.get(id=idAyudante)
                alumno = request.user
                reporte = ReporteAbusoAyudante(reportador=alumno, ayudante=ayudante, motivo=form.cleaned_data['motivo'], comentario=form.cleaned_data['comentario'])
                reporte.save()
                return HttpResponse("OK")
            except:
                return HttpResponse("ERROR")
        else:
            return HttpResponse("ERROR")
    else:
        return HttpResponse("ERROR")
    json = simplejson.dumps(message)
    return HttpResponse(json, mimetype='application/json')


def getForm(request, typeName=None, identificador=None):
    data = {}
    data['ident'] = identificador
    if typeName=="abuso_ayudante":
        data['form'] = AbusoForm()
        data['type'] = "ayudantia"
        rend = render_to_response("report.html", data, context_instance=RequestContext(request))
    elif typeName=="abuso_alumno":
        data['form'] = AbusoForm()  
        data['type'] = "alumno"
        rend = render_to_response("report.html", data, context_instance=RequestContext(request))
    elif typeName=="evaluacion_ayudante":
        data['form'] = EvalForm()
        data['type'] = "ayudantia"
        rend = render_to_response("eval.html", data, context_instance=RequestContext(request))
    elif typeName=="evaluacion_alumno":
        data['form'] = EvalForm()
        data['type'] = "alumno"
        rend = render_to_response("eval.html", data, context_instance=RequestContext(request))
    else:
        rend = HttpResponse("NOT FOUND")
    message = {"response": "OK", "result":rend.content}
    json = simplejson.dumps(message)
    return HttpResponse(json, mimetype='application/json')
