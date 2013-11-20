from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #url(r'^$', 'main.views.mainView'),
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^chaining/', include('smart_selects.urls')),
    url(r'^cuentas/', include('usuarios.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('main.urls')),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
