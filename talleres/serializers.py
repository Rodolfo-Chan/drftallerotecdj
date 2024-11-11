#serializers.py
from rest_framework import serializers
from datetime import datetime
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


class ReporteSerializer(serializers.ModelSerializer):
    registro_participantes_url = serializers.SerializerMethodField()
    evaluacion_desempeno_url = serializers.SerializerMethodField()

    class Meta:
        model = Reporte
        fields = ['id_reporte', 'registro_participantes', 'registro_participantes_url', 
                  'evaluacion_desempeno', 'evaluacion_desempeno_url', 'id_taller_subgrupo']

    def get_registro_participantes_url(self, obj):
        request = self.context.get('request')
        if obj.registro_participantes and request:
            return request.build_absolute_uri(obj.registro_participantes.url)
        return None

    def get_evaluacion_desempeno_url(self, obj):
        request = self.context.get('request')
        if obj.evaluacion_desempeno and request:
            return request.build_absolute_uri(obj.evaluacion_desempeno.url)
        return None

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
    hora_inicio = serializers.SerializerMethodField()
    hora_final = serializers.SerializerMethodField()

    class Meta:
        model = TalleresSubgrupos
        fields = ['id_taller_registro', 'id_taller_catalogo', 'id_instructor', 'periodo_escolar', 
                  'ubicacion', 'turno_taller', 'hora_inicio', 'hora_final', 'estatus_card', 
                  'dias_taller', 'puntos_taller', 'cupo_taller', 'tipo_taller']

    def get_hora_inicio(self, obj):
        if obj.hora_inicio:
            return obj.hora_inicio.strftime("%I:%M %p")  # Formato de 12 horas
        return None

    def get_hora_final(self, obj):
        if obj.hora_final:
            return obj.hora_final.strftime("%I:%M %p")  # Formato de 12 horas
        return None

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