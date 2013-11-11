from __future__ import unicode_literals
from django.db import models
from smart_selects.db_fields import ChainedForeignKey 

class Region(models.Model):
    nombre = models.CharField(max_length=30L, blank=True)

    def __unicode__(self):
        return self.nombre

class Ciudad(models.Model):
    nombre = models.CharField(max_length=100L, blank=True)
    region = models.ForeignKey('region', null=True, blank=True)
    
    def __unicode__(self):
        return self.nombre

class Institucion(models.Model):
    nombre = models.CharField(max_length=60L)
    region = models.ForeignKey(Region, null=True, blank=True)
    ciudad = ChainedForeignKey(
        Ciudad, 
        chained_field="region",
        chained_model_field="region", 
        show_all=False, 
        auto_choose=True,
        null=True, 
        blank=True
    )

    def __unicode__(self):
        return self.nombre
