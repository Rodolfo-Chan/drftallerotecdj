from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *

class AlumnoViewSet(viewsets.ModelViewSet):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer

class InstructorViewSet(viewsets.ModelViewSet):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer

class InscripcionViewSet(viewsets.ModelViewSet):
    queryset = Inscripcion.objects.all()
    serializer_class = InscripcionSerializer

class LocacionViewSet(viewsets.ModelViewSet):
    queryset = Locacion.objects.all()
    serializer_class = LocacionSerializer

class PeriodoViewSet(viewsets.ModelViewSet):
    queryset = Periodo.objects.all()
    serializer_class = PeriodoSerializer

class HorarioViewSet(viewsets.ModelViewSet):
    queryset = Horario.objects.all()
    serializer_class = HorarioSerializer

class UsuarioAdminViewSet(viewsets.ModelViewSet):
    queryset = UsuarioAdmin.objects.all()
    serializer_class = UsuarioAdminSerializer

# Vistas para Talleres_Supergrupo y Talleres_Subgrupos

class TalleresSupergrupoViewSet(viewsets.ModelViewSet):
    queryset = TalleresSupergrupo.objects.all()
    serializer_class = TalleresSupergrupoSerializer

class TalleresSubgruposViewSet(viewsets.ModelViewSet):
    queryset = TalleresSubgrupos.objects.all()
    serializer_class = TalleresSubgruposSerializer

# Agregamos la nueva vista para ConstanciaLiberacion
class ConstanciaLiberacionViewSet(viewsets.ModelViewSet):
    queryset = ConstanciaLiberacion.objects.all()
    serializer_class = ConstanciaLiberacionSerializer

# Agregamos la nueva vista para Reporte
class ReporteViewSet(viewsets.ModelViewSet):
    queryset = Reporte.objects.all()
    serializer_class = ReporteSerializer
