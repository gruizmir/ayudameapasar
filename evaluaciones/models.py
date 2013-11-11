from __future__ import unicode_literals
from django.db import models
from ayudantias.models import Ayudantia

class PuntuacionAyudantes(models.Model):
    puntaje = models.IntegerField(default=1)
    fecha = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    ayudantia = models.ForeignKey(Ayudantia)

    class Meta:
        verbose_name="Puntuación de ayudantía"
        verbose_name_plural="Puntuaciones de ayudantías"

class PuntuacionAlumno(models.Model):
    puntaje = models.IntegerField(default=1)
    fecha = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    usuario = models.ForeignKey(User)

    class Meta:
        verbose_name="Puntuación de Alumno"
        verbose_name_plural="Puntuaciones de alumnos"

class MotivoAbuso(models.Model):
    nombre = models.CharField(max_length=30L)

    class Meta:
        verbose_name="Motivo de abuso"
        verbose_name_plural="Motivos de abuso"

    def __unicode__(self):
        return self.nombre
    
class ReporteAbusoAyudante(models.Model):
    motivo = models.ForeignKey(MotivoAbuso)
    fecha = models.DateTimeField(auto_now_add=True)
    comentario = models.TextField()
    ayudante = models.ForeignKey(Ayudante)
    reportador = models.ForeignKey(User)

    class Meta:
        verbose_name="Reporte de abuso por parte de ayudante"
        verbose_name_plural="Reportes de abuso (ayudantes)"

    def __unicode__(self):
        return self.ayudante.usuario.get_full_name() + ": " +  self.motivo.nombre
    
class ReporteAbusoAlumno(models.Model):
    motivo = models.ForeignKey(MotivoAbuso)
    fecha = models.DateTimeField(auto_now_add=True)
    comentario = models.TextField()
    alumno = models.ForeignKey(User)
    reportador = models.ForeignKey(Ayudante)
    
    class Meta:
        verbose_name="Reporte de abuso por parte de alumnos"
        verbose_name_plural="Reportes de abuso (alumnos)"

    def __unicode__(self):
        return self.alumno.get_full_name() + ": " +  self.motivo.nombre
