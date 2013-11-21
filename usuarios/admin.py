from django.contrib import admin
from usuarios.models import *
from ayudantias.models import *
from django.contrib.sites.models import Site
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin

class UserProfileInline(admin.StackedInline):
    model = Perfil
    max_num = 1
    can_delete = False

class UserAdmin(AuthUserAdmin):
    inlines = [UserProfileInline]
    
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Ayudante)
admin.site.register(AnuncioGeneral)
admin.site.register(InfoAcademica)
admin.site.register(Categoria)
admin.site.register(Subcategoria)
admin.site.register(Ayudantia)
admin.site.register(HorarioAyudantia)
admin.site.register(AlumnoAyudantia)
admin.site.unregister(Site)
