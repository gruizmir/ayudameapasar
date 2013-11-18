from django.conf.urls.defaults import *

urlpatterns = patterns('usuarios.views',
    url(r'^confirmar/(\w+)$', 'confirm'),
    url(r'^(?P<idUser>\d+)/perfil', 'mostrarPerfil'),
    url(r'^perfil', 'mostrarPerfilPropio'),
    url(r'^login', 'loginView'),
    url(r'^logout', 'logoutView'),
    url(r'^registro', 'registerView'),
)
