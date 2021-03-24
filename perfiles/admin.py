from django.contrib import admin

# Register your models here.
from .models import Perfil
from .models import Hipertension

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'bio', 'web')


@admin.register(Hipertension)
class HipertensionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'presion_s', 'edad', 'genero', 'imc', 'presion_d', 'colesterol_t')