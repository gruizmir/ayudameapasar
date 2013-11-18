# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from smart_selects.db_fields import ChainedForeignKey 

class Region(models.Model):
    nombre = models.CharField(max_length=30L, blank=True)
    numero = models.CharField(max_length=2L, blank=True)
    
    class Meta:
        verbose_name="Región"
        verbose_name_plural="Regiones"
    
    def __unicode__(self):
        return self.nombre

class Ciudad(models.Model):
    nombre = models.CharField(max_length=100L, blank=True)
    region = models.ForeignKey(Region, null=True, blank=True)
    
    class Meta:
        verbose_name_plural="Ciudades"
        
    def __unicode__(self):
        return self.nombre

class Institucion(models.Model):
    nombre = models.CharField(max_length=60L)
    region = models.ForeignKey(Region, null=False, blank=False)
    ciudad = ChainedForeignKey(
        Ciudad, 
        chained_field='region',
        chained_model_field='region', 
        show_all=False, 
        auto_choose=True,
        null=False, 
        blank=False
    )

    class Meta:
        verbose_name="Institución"
        verbose_name_plural="Instituciones"
        
    def __unicode__(self):
        return self.nombre


class EmailValidos(models.Model):
    dominio = models.CharField(max_length=20L)
    institucion = models.ForeignKey(Institucion)
    
    class Meta:
        verbose_name="Email válido"
        verbose_name_plural="Dominios email válidos"
        
    def __unicode__(self):
        return "%s - %s" % (self.institucion.nombre, self.dominio)
