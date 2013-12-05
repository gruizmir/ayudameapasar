from django.conf.urls.defaults import *

urlpatterns = patterns('ayudantias.views',
	#url(r'^confirmar/(\w+)$', 'confirm'),
	#url(r'^(?P<idUser>\d+)/perfil', 'mostrarPerfil'),
	url(r'^publicar_ayudantia/$', 'publicar_ayudantia'),
	url(r'^mis_ayudantias/$', 'mis_ayudantias'),
	url(r'^$', 'ayudantias'),
	url(r'^editar_ayudantia/(?P<ayudantia_id>\d+)', 'editar_ayudantia'),
    url(r'^hora/(\d+)/$', 'pedirHora'),
    url(r'^solicitud/(\d+)/$', 'aceptarSolicitud'),
    url(r'^detalles/(\d+)/$', 'getAyudantia'),
)
