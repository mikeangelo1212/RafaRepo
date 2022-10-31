from django.contrib import admin

from trabajador.models import *
# Register your models here.
admin.site.register(Trabajador)
admin.site.register(Domicilio)
admin.site.register(Jefe)
admin.site.register(Departamento)