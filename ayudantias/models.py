# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from usuarios.models import Ayudante
from smart_selects.db_fields import ChainedForeignKey 
from django.contrib.auth.models import User
from datetime import date

ESTADO = ['Publicada','Despublicada']

class Categoria(models.Model):
	nombre = models.CharField(max_length=50L, verbose_name="Categoría")
	
	def __unicode__(self):
		return self.nombre
		
class Subcategoria(models.Model):
	nombre = models.CharField(max_length=50L, verbose_name="Categoría")
	categoria = models.ForeignKey(Categoria)
	
	def __unicode__(self):
		return self.nombre

class Ayudantia(models.Model):
	ayudante = models.ForeignKey(Ayudante)
	nombre = models.CharField(max_length=50L, verbose_name="Nombre del ramo")
	descripcion = models.TextField()
	ESTADOS = (
			 ("1", "Publicado"),
			 ("2", "Despublicado"),
			 ("3", "Baneado")
			)
	estado = models.CharField(max_length=1, choices=ESTADOS, default="1")
	fecha_publicacion = models.DateTimeField(auto_now_add=True)
	fecha_termino = models.DateTimeField()
	categoria = models.ForeignKey(Categoria, null=True, blank=True)
	subcategoria = ChainedForeignKey(
		Subcategoria, 
		chained_field="categoria",
		chained_model_field="categoria", 
		show_all=False, 
		auto_choose=True,
		null=True, 
		blank=True
	)
	costo_por_hora = models.IntegerField()

	def __unicode__(self):
		return self.nombre

	# Metodos
	def GetAyudantias(self):
		fecha_actual = date.today()
		return Ayudantia.objects.filter(fecha_termino__gte=fecha_actual, estado="1").order_by('-fecha_publicacion')

	def GetAyudantiasAyudante(self, ayudante):
		return Ayudantia.objects.filter(ayudante=ayudante).order_by('-fecha_publicacion', '-fecha_termino')

class HorarioAyudantia(models.Model):
	ayudantia = models.ForeignKey(Ayudantia)
	hora_inicio = models.TimeField(verbose_name="Hora de inicio")
	hora_final = models.TimeField(verbose_name="Hora de finalización")
	DIAS = (("1", "Lunes"),
		("2", "Martes"),
		("3", "Miercoles"),
		("4", "Jueves"),
		("5", "Viernes"),
		("6", "Sábado"),
		("7", "Domingo"),
		)
	dia = models.CharField(max_length=1, choices=DIAS, default="1")
	activo = models.BooleanField(default=True)

	def __unicode__(self):
		return self.ayudantia.nombre
	
class AlumnoAyudantia(models.Model):
	alumno = models.ForeignKey(User)
	ayudantia = models.ForeignKey(Ayudantia)
	horario = models.ForeignKey(HorarioAyudantia)
	asistio = models.BooleanField(default=False)
	aceptada = models.BooleanField(default=False)
	fecha_solicitud = models.DateTimeField(auto_now_add=True)
	cantidad_personas = models.IntegerField(default=1, verbose_name="Cantidad de asistentes")
	
	def __unicode__(self):
		return self.alumno.get_full_name()
