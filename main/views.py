# Create your views here.
from __future__ import unicode_literals
from ayudantias.models import Ayudantia
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core import mail
from django.core.context_processors import csrf
from django.core.exceptions import ObjectDoesNotExist, PermissionDenied, SuspiciousOperation
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from main.models import Institucion
from usuarios.models import Perfil, Ayudante, UsuarioPorConfirmar, InfoAcademica
from usuarios.forms import RegisterForm, LoginForm
import uuid


def landing(request):
	dict = {}

	dict['hola'] = "hola"
	return render_to_response("landing.html", dict, context_instance=RequestContext(request))