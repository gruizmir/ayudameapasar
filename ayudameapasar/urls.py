from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #url(r'^$', 'main.views.mainView'),
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^chaining/', include('smart_selects.urls')),
    url(r'^login', 'usuarios.views.loginView'),
    url(r'^logout', 'usuarios.views.logoutView'),
    url(r'^register', 'usuarios.views.registerView'),
    url(r'^cuentas/confirmar/(\w+)$', 'usuarios.views.confirm'),
    url(r'^admin/', include(admin.site.urls)),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
