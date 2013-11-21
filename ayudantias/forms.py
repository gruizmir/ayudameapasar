# -*- coding: utf-8 -*-
from django.forms import Form, ModelForm, BooleanField, ChoiceField, CharField, TextInput, BooleanField, ModelChoiceField, Select, CheckboxInput, ValidationError, Textarea, DateField, TimeField
from ayudantias.models import *

class publicarAyudantiaForm(ModelForm):
	nombre = CharField(required=True, label="Nombre", widget=TextInput(attrs={'class':'form-control'}))
	descripcion = CharField(required=True, label="Descripcion", widget=Textarea(attrs={'class':'form-control'}))
	categoria = ModelChoiceField(required=True, 
		queryset=Categoria.objects.all(),
		initial=0,
		widget=Select(attrs={'class':'form-control'}))

	subcategoria = ModelChoiceField(required=True, 
		queryset=Subcategoria.objects.all(),
		initial=0,
		widget=Select(attrs={'class':'form-control'}))

	fecha_termino = DateField(widget=TextInput(attrs={'class':'form-control'}))

	class Meta:
		model = Ayudantia
		exclude = ('ayudante', 'estado')


class horarioAyudantiaForm(ModelForm):
	hora_inicio = TimeField(required=True, widget=TextInput(attrs={'class':'form-control'}))
	hora_final = TimeField(required=True, widget=TextInput(attrs={'class':'form-control'}))

	DIAS = [("1", "Lunes"),
		("2", "Martes"),
		("3", "Miercoles"),
		("4", "Jueves"),
		("5", "Viernes"),
		("6", "Sábado"),
		("7", "Domingo"),
		]
	
	dia = ChoiceField(required=True, label="Dias", choices=DIAS, widget=Select(attrs={'class':'form-control'}))

	class Meta:
		model = HorarioAyudantia
		exclude = ('ayudantia', 'activo')