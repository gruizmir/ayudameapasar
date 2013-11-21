# -*- coding: utf-8 -*-
from django.forms import Form, ModelForm, ChoiceField, CharField, TextInput, ModelChoiceField, Select, ValidationError, Textarea, DateField, TimeField, IntegerField
from ayudantias.models import *

class publicarAyudantiaForm(ModelForm):
	nombre = CharField(required=True, label="Nombre", widget=TextInput(attrs={'class':'form-control'}))
	descripcion = CharField(required=True, label="Descripción", widget=Textarea(attrs={'class':'form-control'}))
	categoria = ModelChoiceField(required=True,
		queryset=Categoria.objects.all(),
		initial=0,
		widget=Select(attrs={'class':'form-control'}),
		empty_label="-------------")

	subcategoria = ModelChoiceField(required=True, 
		queryset=Subcategoria.objects.all(),
		initial=0,
		widget=Select(attrs={'class':'form-control'}),
		empty_label="-------------")
	costo_por_hora = IntegerField(widget=TextInput(attrs={'class':'form-control money-field'}))
	fecha_termino = DateField(widget=TextInput(attrs={'class':'form-control'}))

	class Meta:
		model = Ayudantia
		exclude = ('ayudante', 'estado')


class horarioAyudantiaForm(ModelForm):
	hora_inicio = TimeField(required=True, label="Hora de Inicio", widget=TextInput(attrs={'class':'form-control'}))
	hora_final = TimeField(required=True, label="Hora de finalización", widget=TextInput(attrs={'class':'form-control'}))

	DIAS = [("1", "Lunes"),
		("2", "Martes"),
		("3", "Miercoles"),
		("4", "Jueves"),
		("5", "Viernes"),
		("6", "Sábado"),
		("7", "Domingo"),
		]
	
	dia = ChoiceField(required=True, label="Día", choices=DIAS, widget=Select(attrs={'class':'form-control'}))

	class Meta:
		model = HorarioAyudantia
		exclude = ('ayudantia', 'activo')