from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('alumnos', AlumnoViewSet)
router.register('instructores', InstructorViewSet)
router.register('inscripciones', InscripcionViewSet)
router.register('locaciones', LocacionViewSet)
router.register('periodos', PeriodoViewSet)
router.register('horarios', HorarioViewSet)
router.register('usuarioAdmin', UsuarioAdminViewSet)
router.register('talleres_supergrupo', TalleresSupergrupoViewSet)
router.register('talleres_subgrupos', TalleresSubgruposViewSet)
router.register('constancias_liberacion', ConstanciaLiberacionViewSet)  # Nueva vista registrada
router.register('reportes', ReporteViewSet)  # Nueva vista para Reporte
router.register('nivel_acceso', NivelAccesoViewSet)  # Nueva vista registrada para NivelAcceso


urlpatterns = [
    path('api/', include(router.urls)),
]
