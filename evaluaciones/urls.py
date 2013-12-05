from django.conf.urls.defaults import *

urlpatterns = patterns('evaluaciones.views',
	url(r'^ayudantia/(\d+)/$', 'evalAyudantia'),
	url(r'^alumno/(\d+)/$', 'evalAlumno'),
    url(r'^reporte/ayudantia/(\d+)/$', 'abusoAyudante'),
    url(r'^reporte/alumno/(\d+)/$', 'abusoAlumno'),
    url(r'^reporte/anuncio/(\d+)/$', 'abusoAnuncio'),
    url(r'^getform/(\w+)/(\d+)$', 'getForm'),
)
