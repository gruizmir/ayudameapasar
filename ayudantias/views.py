# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.core.exceptions import ObjectDoesNotExist, PermissionDenied, SuspiciousOperation
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.utils import simplejson

from ayudantias.models import *
from usuarios.models import Ayudante, Perfil
from ayudantias.forms import *

# muestra todas las ayudantias 
def ayudantias(request):
	data = {}
	data['lista_ayudantias'] = Ayudantia.objects.all()
	return render_to_response("ayudantias.html", data, context_instance=RequestContext(request))

# trae solo las ayudantias del usuario
@login_required
def mis_ayudantias(request):
	data = {}
	data['lista_ayudantias'] = None

	# obtiene el usuario
	user = request.user

	# determina si es ayudante
	if user.perfil.es_ayudante:
		try:
			ayudante = Ayudante.objects.get(usuario=user)
			data['lista_ayudantias'] = Ayudantia().GetAyudantiasAyudante(ayudante)
		except ObjectDoesNotExist:
			pass
			#TO-DO

	return render_to_response("mis_ayudantias.html", data, context_instance=RequestContext(request))


@login_required
def publicar_ayudantia(request):
	data = {}

	if request.method == 'POST':
		formulario_ayudantia = publicarAyudantiaForm(request.POST)
		formulario_horario = horarioAyudantiaForm(request.POST)
		
		if formulario_ayudantia.is_valid() and formulario_horario.is_valid():
			ayudantia = formulario_ayudantia.save(commit=False)
			horario = formulario_horario.save(commit=False)

			# extrae el usuario
			# si es un ayudante
			user = request.user
			
			if user.perfil.es_ayudante:
				try:
					ayudante = Ayudante.objects.get(usuario=user)
				except ObjectDoesNotExist:
					messages.error(request, "Error al intentar obtener sus datos.")
					data['ayudantiaForm'] = formulario_ayudantia
					data['horarioForm'] = formulario_horario
					return render_to_response("publicar_ayudantia.html", data, context_instance=RequestContext(request))
			else:
				ayudante = user.perfil.crear_ayudante()

			# almacena el ayudante
			ayudantia.ayudante = ayudante
			ayudantia.save()
			horario.ayudantia = ayudantia
			horario.save()

			messages.success(request, "Se ha agregado correctamente el aviso de ayudantía")
			return HttpResponseRedirect("/ayudantias/")
		else:
			messages.error(request, "Error al ingresar ayudantia, revise bien los campos!")
	else:
		formulario_ayudantia = publicarAyudantiaForm()
		formulario_horario = horarioAyudantiaForm()

	data['ayudantiaForm'] = formulario_ayudantia
	data['horarioForm'] = formulario_horario
	return render_to_response("publicar_ayudantia.html", data, context_instance=RequestContext(request))

@login_required
def editar_ayudantia(request, ayudantia_id):
	data = {}

	ayudantia = Ayudantia().GetAyudantia(ayudantia_id)
	if ayudantia is None:
		messages.error(request, "La ayudantia no existe...")
		return HttpResponseRedirect("/ayudantias/")

	horario = ayudantia.horarioayudantia_set.all()[0]

	if request.method == 'POST':
		formulario_ayudantia = publicarAyudantiaForm(request.POST, instance=ayudantia)
		formulario_horario = horarioAyudantiaForm(request.POST, instance=horario)
		
		if formulario_ayudantia.is_valid() and formulario_horario.is_valid():
			ayudantia = formulario_ayudantia.save(commit=False)
			horario = formulario_horario.save(commit=False)
			ayudantia.save()
			horario.save()

			messages.success(request, "Se ha actualizado correctamente el aviso de ayudantía")
			return HttpResponseRedirect("/ayudantias/")
		else:
			messages.error(request, "Error al actualizar ayudantia, revise bien los campos!")
	else:
		formulario_ayudantia = publicarAyudantiaForm(instance = ayudantia)
		formulario_horario = horarioAyudantiaForm(instance = horario)

	data['ayudantia_id'] = ayudantia_id
	data['ayudantiaForm'] = formulario_ayudantia
	data['horarioForm'] = formulario_horario
	return render_to_response("editar_ayudantia.html", data, context_instance=RequestContext(request))


def pedirHora(request, idAyudantia=None):
	if request.is_ajax():
		alumno = request.user
		try:
			ayudantia = Ayudantia.objects.get(id=idAyudantia)
			horario = HorarioAyudantia.objects.filter(ayudantia=ayudantia)
			if horario.exists():
				print horario
				print list(horario)[0]
				solicitud = AlumnoAyudantia(alumno=alumno, ayudantia=ayudantia, horario=list(horario)[0])
				solicitud.save()
				
				message = {"response": "OK", "result":""}
			else:
				message = {"response": "ERROR", "result":"HORARIO NOT FOUND"}
		except:
			message = {"response": "ERROR", "result":"404"}
	else:
		raise Http404
	json = simplejson.dumps(message)
	return HttpResponse(json, mimetype='application/json')

def aceptarSolicitud(request, idAlumnoAyudantia=None):
	if request.is_ajax():
		alumno = request.user
		try:
			solicitud = AlumnoAyudantia.objects.get(id=idAlumnoAyudantia)
			if solicitud:
				solicitud.aceptada = True
				solicitud.save()
				
				message = {"response": "OK", "result":""}
			else:
				message = {"response": "ERROR", "result":"Solicitud NOT FOUND"}
		except:
			message = {"response": "ERROR", "result":"404"}
	else:
		raise Http404
	json = simplejson.dumps(message)
	return HttpResponse(json, mimetype='application/json')