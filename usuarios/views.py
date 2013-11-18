# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from usuarios.models import Perfil, Ayudante
from usuarios.forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.core.exceptions import ObjectDoesNotExist, PermissionDenied, SuspiciousOperation
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

def loginView(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if 'next' in request.GET:
            redir = request.GET['next']
        else:
            redir=None
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(username=email, password=password)
            if user is not None:
                login(request,user)
                if redir is not None:
                    return HttpResponseRedirect(redir)
                else:
                    return HttpResponseRedirect("/perfil")
        else:
            return render_to_response("login.html", {'form':form}, context_instance=RequestContext(request))
    else:
        form = LoginForm()
        return render_to_response("login.html", {'form':form}, context_instance=RequestContext(request))


def registerView(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("/")
        else:
            return render_to_response("register.html", {'form':form}, context_instance=RequestContext(request))
    else:
        form = RegisterForm()
        return render_to_response("register.html", {'form':form}, context_instance=RequestContext(request))

def logoutView(request):
    logout(request)
