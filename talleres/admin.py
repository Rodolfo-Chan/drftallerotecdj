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
    TalleresSupergrupo,    # Importar TalleresSupergrupo
    TalleresSubgrupos,     # Importar TalleresSubgrupos
    ConstanciaLiberacion,  # Importar ConstanciaLiberacion
    Reporte                # Importar Reporte
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
admin.site.register(TalleresSupergrupo)  # Registrar TalleresSupergrupo
admin.site.register(TalleresSubgrupos)   # Registrar TalleresSubgrupos
admin.site.register(ConstanciaLiberacion)  # Registrar ConstanciaLiberacion
admin.site.register(Reporte)  # Registrar Reporte
