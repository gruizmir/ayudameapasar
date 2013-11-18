# -*- coding: utf-8 -*-
from django.forms import Form, ModelForm, BooleanField, CharField, EmailField, IntegerField, TextInput, Textarea, BooleanField, ImageField, ModelChoiceField, PasswordInput, Select, CheckboxInput
from django.db import models
from django.contrib.auth.models import User
from main.models import Institucion
from django.contrib.auth.hashers import (
    MAXIMUM_PASSWORD_LENGTH, UNUSABLE_PASSWORD, identify_hasher,
)

class RegisterForm(Form):
    error_messages = {
        'duplicate_email': "Email ya registrado",
        'password_mismatch': "Contraseñas no coinciden",
    }
    nombre = CharField(required=True, label="Nombre", widget=TextInput(attrs={'class':'form-control'}))
    apellido = CharField(required=True, label="Apellido(s)", widget=TextInput(attrs={'class':'form-control'}))
    email = EmailField(required=True, help_text="Debe ser tu email institucional", widget=TextInput(attrs={'class':'form-control'}))
    password1 = CharField(
        label="Contraseña",
        required=True,
        max_length=MAXIMUM_PASSWORD_LENGTH,
        widget=PasswordInput(attrs={'class':'form-control'})
    )
    password2 = CharField(
        label="Confirme Contraseña",
        required=True,
        max_length=MAXIMUM_PASSWORD_LENGTH,
        widget=PasswordInput(attrs={'class':'form-control'})
    )
    institucion = ModelChoiceField(required=True,
        queryset=Institucion.objects.all(),
        initial=0,
        help_text="Por el momento, sólo disponible para usuarios de la UTFSM",
        widget=Select(attrs={'class':'form-control'})
    )
    es_ayudante = BooleanField(required=False, label="¿Eres ayudante?", widget=CheckboxInput(attrs={'class':'form-control'}))

    def clean_email(self):
        email = self.cleaned_data["email"]
        try:
            User._default_manager.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError(self.error_messages['duplicate_email'])
    
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'])
        return password2
        
class LoginForm(Form):
    email = EmailField(required=True, help_text="Debe ser tu email institucional", widget=TextInput(attrs={'class':'form-control'}))
    password = CharField(
        label="Contraseña",
        required=True,
        max_length=MAXIMUM_PASSWORD_LENGTH,
        widget=PasswordInput(attrs={'class':'form-control'})
    )
    keep = BooleanField(required=False, label="Mantenerme activo")
    
    error_messages = {
        'invalid_login': "Ingrese usuario y contraseña válidos.",
        'no_cookies': "Debe habilitar cookies para iniciar sesión.",
        'inactive': "Cuenta bloqueada.",
    }

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email and password:
            self.user_cache = authenticate(username=email,
                                           password=password)
            if self.user_cache is None:
                raise forms.ValidationError(
                    self.error_messages['invalid_login']
                    )
            elif not self.user_cache.is_active:
                raise forms.ValidationError(self.error_messages['inactive'])
        self.check_for_test_cookie()
        return self.cleaned_data

    def check_for_test_cookie(self):
        if self.request and not self.request.session.test_cookie_worked():
            raise forms.ValidationError(self.error_messages['no_cookies'])

    def get_user_id(self):
        if self.user_cache:
            return self.user_cache.id
        return None

    def get_user(self):
        return self.user_cache
