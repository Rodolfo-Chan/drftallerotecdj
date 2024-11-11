#models.py

from django.db import models
from django.core.validators import RegexValidator
import random
import string

# Función para generar contraseñas aleatorias
def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

# Modelo para la tabla NivelAcceso
class NivelAcceso(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    nivel = models.IntegerField(unique=True)  # Nivel numérico de acceso, donde menor número = menor acceso

    def __str__(self):
        return self.nombre

# Modelo para la tabla UsuarioAdmin
class UsuarioAdmin(models.Model):
    id_admin = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)
    contraseña = models.CharField(max_length=128, editable=False)  # Campo de contraseña, no editable
    nivel_acceso = models.ForeignKey(NivelAcceso, on_delete=models.CASCADE, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.contraseña:  # Generar contraseña solo si no existe
            self.contraseña = generate_password()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.nombre} {self.apellido_paterno} {self.apellido_materno}'

# Modelo para la tabla Alumnos
class Alumno(models.Model):
    #id_alumno = models.AutoField(primary_key=True)
    id_alumno = models.AutoField(primary_key=True)  # Use AutoField for an identity column

    matricula_alumno = models.CharField(
        max_length=8,
        validators=[RegexValidator(r'^\d{8}$', 'La matrícula debe tener exactamente 8 dígitos.')],
        unique=True
    )
    nombre = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    genero = models.CharField(max_length=10)
    carrera = models.CharField(max_length=100)
    semestre = models.IntegerField()
    email = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=128, editable=False)
    nivel_acceso = models.ForeignKey(NivelAcceso, on_delete=models.SET_NULL, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.nivel_acceso:
            nivel_acceso_bajo, created = NivelAcceso.objects.get_or_create(nombre='Alumno', defaults={'nivel': 1})
            self.nivel_acceso = nivel_acceso_bajo
        if not self.contraseña:
            self.contraseña = generate_password()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.nombre} {self.apellido_paterno} {self.apellido_materno}'

# Modelo para la tabla RubricaReportes
class RubricaReportes(models.Model):
    id_rubrica_reporte = models.AutoField(primary_key=True)
    registro_de_participantes = models.FileField(upload_to='rubricas/participantes/', blank=True, null=True)  # Almacenar archivo PDF
    evaluacion_desempeno = models.FileField(upload_to='rubricas/evaluacion/', blank=True, null=True)  # Almacenar archivo PDF

    def __str__(self):
        return f'Rúbrica {self.id_rubrica_reporte}'

# Modelo para la tabla Instructores
class Instructor(models.Model):
    id_instructor = models.AutoField(primary_key=True)
    #id_rubrica_reporte = models.ForeignKey(RubricaReportes, on_delete=models.SET_NULL, null=True, blank=True)
    nombre = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(unique=True)  # Campo de email
    contraseña = models.CharField(max_length=128, editable=False)  # Campo de contraseña, no editable
    genero = models.CharField(max_length=10)
    tipo = models.CharField(max_length=20)  # Estudiante o Profesor
    estatus = models.CharField(max_length=10)  # Activo o Inactivo
    nivel_acceso = models.ForeignKey(NivelAcceso, on_delete=models.SET_NULL, null=True, blank=True)

    def save(self, *args, **kwargs):
        # Asignar nivel de acceso (Profesor) si no se proporciona uno
        if not self.nivel_acceso:
            # Verificar si el nivel de acceso 'Profesor' existe
            nivel_acceso_profesor, created = NivelAcceso.objects.get_or_create(nombre='Profesor', defaults={'nivel': 2})
            self.nivel_acceso = nivel_acceso_profesor
        
        if not self.contraseña:  # Generar contraseña solo si no existe
            self.contraseña = generate_password()
        
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.nombre} {self.apellido_paterno} {self.apellido_materno}'

# Modelo para la tabla Talleres_Supergrupo
class TalleresSupergrupo(models.Model):
    id_taller_catalogo = models.AutoField(primary_key=True)
    nombre_taller = models.CharField(max_length=100)
    estatus_taller = models.BooleanField(default=True)  # True si está activo, False si no

    def __str__(self):
        return self.nombre_taller

# Modelo para la tabla Talleres_Subgrupos
from django.db import models

# Modelo para la tabla Talleres_Subgrupos
class TalleresSubgrupos(models.Model):
    id_taller_registro = models.AutoField(primary_key=True)
    id_taller_catalogo = models.ForeignKey('TalleresSupergrupo', on_delete=models.CASCADE)
    id_instructor = models.ForeignKey('Instructor', on_delete=models.CASCADE)
    periodo_escolar = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)
    turno_taller = models.CharField(max_length=50)
    hora_inicio = models.TimeField()
    hora_final = models.TimeField()
    estatus_card = models.BooleanField(default=True)
    dias_taller = models.CharField(max_length=200)
    puntos_taller = models.IntegerField()
    cupo_taller = models.IntegerField()
    tipo_taller = models.CharField(max_length=100)

    @property
    def hora_inicio_formateada(self):
        return self.hora_inicio.strftime('%H:%M')

    @property
    def hora_final_formateada(self):
        return self.hora_final.strftime('%H:%M')

    def __str__(self):
        return f'{self.id_taller_catalogo} - {self.tipo_taller}'


# Modelo para la tabla Inscripciones
class Inscripcion(models.Model):
    id_inscripcion = models.AutoField(primary_key=True)
    id_alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    id_taller_registro = models.ForeignKey(TalleresSubgrupos, on_delete=models.CASCADE)
    estatus = models.CharField(max_length=20)

    def __str__(self):
        return f'Inscripción de {self.id_alumno} en {self.id_taller_registro}'

# Modelo para la tabla Locaciones
class Locacion(models.Model):
    id_locacion = models.AutoField(primary_key=True)
    nombre_locacion = models.CharField(max_length=100)
    descripcion_locacion = models.TextField()

    def __str__(self):
        return self.nombre_locacion

# Modelo para la tabla Periodos
class Periodo(models.Model):
    id_periodo = models.AutoField(primary_key=True)
    periodo_taller = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    def __str__(self):
        return self.periodo_taller

# Modelo para la tabla Horarios
class Horario(models.Model):
    id_horario = models.AutoField(primary_key=True)
    dias = models.CharField(max_length=50)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    def __str__(self):
        return f'Horario: {self.dias} de {self.hora_inicio} a {self.hora_fin}'

# Modelo para la tabla Constancia Liberacion 
class ConstanciaLiberacion(models.Model):
    id_constancia = models.AutoField(primary_key=True)
    id_alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    fecha_emision = models.DateField(auto_now_add=True)
    contancia_liberacion = models.FileField(upload_to='contancia/liberacion/', blank=True, null=True)

    def __str__(self):
        return f'Constancia {self.id_constancia} - Alumno: {self.id_alumno}'

# Modelo para la tabla Reportes y archivos 
class Reporte(models.Model):
    id_reporte = models.AutoField(primary_key=True)
    id_taller_subgrupo = models.ForeignKey(TalleresSubgrupos, on_delete=models.CASCADE)  # Clave foránea a TalleresSubgrupos
    registro_participantes = models.FileField(upload_to='reportes/participantes/', blank=True, null=True)
    evaluacion_desempeno = models.FileField(upload_to='reportes/evaluacion/', blank=True, null=True)

    def __str__(self):
        return f'Reporte {self.id_reporte} - Taller Subgrupo: {self.id_taller_subgrupo}'

