from __future__ import unicode_literals
from django.db import models
from usuarios.models import Ayudante

ESTADO = ['Publicada','Despublicada']

class Ayudantia(models.Model):
    ayudante = models.ForeignKey(Ayudante)
    nombre = models.CharField(max_length=50L, verbose_name="Nombre del ramo")
    descripcion = models.TextField()
    estado = models.IntegerField(default=0)

    def __unicode__(self):
        return self.nombre

class HorarioAyudantia(models.Model):
    ayudantia = models.ForeignKey(Ayudantia)
    hora_inicio = models.TimeField(verbose_name="Hora de inicio")
    hora_final = models.TimeField(verbose_name="Hora de finalización")
    dia = models.IntegerField(default=1)
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
