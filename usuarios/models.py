from __future__ import unicode_literals
from django.db import models
from main.models import Institucion

class Perfil(models.Model):
    usuario = models.OneToOneField(User, unique=True)
    institucion = models.ForeignKey(Institucion)
    avatar = models.ImageField(blank=True, upload_to='user_pics', default='/static/img/profile_picture.png')
    puntuacion = models.FloatField(default=0.0)
    eval_qty = models.IntegerField(default=0)
    fono = models.CharField(max_length=15L)
    
    class Meta:
        verbose_name_plural="Perfiles"
        
    def __unicode__(self):
        return self.user.get_full_name()
    
User.perfil = property(lambda u: Perfil.objects.get_or_create(user=u)[0])


class Ayudante(models.Model):
    usuario = models.OneToOneField(User, primary_key=False)
    puntuacion = models.FloatField(default=0.0)
    eval_qty = models.IntegerField(default=0)

    def __unicode__(self):
        return self.user.get_full_name()


class InfoAcademica(models.Model):
    ayudante = models.ForeignKey(Ayudante)
    nombre_ramo = models.CharField(max_length=50L, verbose_name="Nombre del ramo")
    carrera = models.CharField(max_length=50L)
    tpo_experiencia = models.IntegerField(default=1, verbose_name="Semestres de experiencia", help_text="Si el ramo es anual, marca 2 semestres por cada año.")

    class Meta:
        verbose_name="Información Académica"
        verbose_name_plural="Informaciones Académicas"

    def __unicode__(self):
        return self.ayudante.usuario.get_full_name()
    
class AnuncioGeneral(models.Model):
    titulo = models.CharField(max_length=50L, verbose_name="Nombre del ramo")
    mensaje = models.TextField()
    enviar_email = models.BooleanField(default=False)
    hora_publicacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(Usuario)
    
    def __unicode__(self):
        return self.titulo
