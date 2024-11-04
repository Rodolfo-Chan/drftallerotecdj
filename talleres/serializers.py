from rest_framework import serializers
from .models import (
    Alumno,
    Instructor,
    Inscripcion,
    Locacion,
    Periodo,
    Horario,
    UsuarioAdmin,
    TalleresSupergrupo,    
    TalleresSubgrupos,
    ConstanciaLiberacion,  # Agregamos la nueva tabla
    Reporte,
    NivelAcceso,               # Importamos la nueva tabla Reporte
    RubricaReportes
)

class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = '__all__'

class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = '__all__'

class InscripcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inscripcion
        fields = '__all__'

class LocacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locacion
        fields = '__all__'

class PeriodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Periodo
        fields = '__all__'

class HorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horario
        fields = '__all__'

class TalleresSupergrupoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TalleresSupergrupo  
        fields = '__all__'

class TalleresSubgruposSerializer(serializers.ModelSerializer):
    class Meta:
        model = TalleresSubgrupos  
        fields = '__all__'

class UsuarioAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioAdmin
        fields = '__all__'

class ConstanciaLiberacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConstanciaLiberacion
        fields = '__all__'

# Agregamos el nuevo serializer para Reporte
class ReporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reporte
        fields = '__all__'

class NivelAccesoSerializer(serializers.ModelSerializer):
    class Meta:
        model = NivelAcceso
        fields = '__all__'  # O puedes especificar los campos que quieras incluir
class RubricaReportesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RubricaReportes
        fields = '__all__'