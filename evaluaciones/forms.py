# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from evaluaciones.models import ReporteAbusoAyudante, ReporteAbusoAlumno, MotivoAbuso
from django.forms import Form, CharField, IntegerField, ModelChoiceField, Select, TextInput, Textarea

class EvalForm(Form):
    puntaje = IntegerField(required=True, label="Puntaje", widget=TextInput(attrs={'class':'form-control'}))
    descripcion = CharField(required=True, label="Descripción", widget=Textarea(attrs={'class':'form-control'}))
    
class AbusoForm(Form):
    motivo = ModelChoiceField(required=True,
        label="Motivo",
        queryset=MotivoAbuso.objects.all(),
        initial=0,
        widget=Select(attrs={'class':'form-control'})
    )
    comentario = CharField(required=True, label="Comentario", widget=Textarea(attrs={'class':'form-control'}))


