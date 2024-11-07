#admin.py
from django.contrib import admin
from .models import (
    Alumno,
    Inscripcion,
    Instructor,
    Locacion,
    Periodo,
    Horario,
    UsuarioAdmin,
    NivelAcceso,
    TalleresSupergrupo,
    TalleresSubgrupos,
    ConstanciaLiberacion,
    Reporte,
    RubricaReportes  # Importar RubricaReportes
)

# Registrar cada modelo en el panel de administración
admin.site.register(Alumno)
admin.site.register(Inscripcion)
admin.site.register(Instructor)
admin.site.register(Locacion) 
admin.site.register(Periodo)
admin.site.register(Horario)
admin.site.register(UsuarioAdmin)
admin.site.register(NivelAcceso)
admin.site.register(TalleresSupergrupo)
admin.site.register(TalleresSubgrupos)
admin.site.register(ConstanciaLiberacion)
admin.site.register(Reporte)
admin.site.register(RubricaReportes)  
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido_paterno', 'apellido_materno', 'fecha_inscripcion')
    search_fields = ('nombre', 'apellido_paterno')
    list_filter = ('nivel_acceso',)