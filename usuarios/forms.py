# -*- coding: utf-8 -*-
from django.forms import Form, ModelForm, BooleanField, CharField, EmailField, IntegerField, TextInput, Textarea, BooleanField, ImageField, ModelChoiceField, PasswordInput
from django.db import models
from django.contrib.auth.models import User
from main.models import Institucion

class NewUserForm(Form):
    nombre = CharField(required=True, label="Nombre", required=True, widget=TextInput(attrs={'class':'form-control'}))
    apellido = CharField(required=True, label="Apellido(s)",required=True, widget=TextInput(attrs={'class':'form-control'}))
    email = EmailField(required=True, help_text="Debe ser tu email institucional", widget=TextInput(attrs={'class':'form-control'}))
    password = CharField(required=True, label="Contraseña",required=True, widget=PasswordInput(attrs={'class':'form-control'}))
    institucion = ModelChoiceField(required=True,
        queryset=Institucion.objects.all(),
        initial=0,
        help_text="Por el momento, sólo disponible para usuarios de la UTFSM",
        widget=Select(attrs={'class':'form-control'})
    )
    es_ayudante = BooleanField(required=False, label="¿Eres ayudante?", widget=CheckboxInput(attrs={'class':'form-control'}))
    
    
