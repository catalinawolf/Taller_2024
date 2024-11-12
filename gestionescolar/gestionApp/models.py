from enum import unique
from django.db import models

class calificacion (models.Model):
    nota = models.IntegerField(null=False, default=0)

class horario (models.Model):
    detallehorario = models.CharField(max_length=20)

class perfil (models.Model):
    id = models.IntegerField(max_length=12, null=False, unique=True)
    
class cargo (models.Model):
    nombre = models.CharField(max_length= 30)

class usuario (models.Model):
    id_perfil = models.IntegerField(max_length=12, null=False, unique=True)
    id_persona = models.IntegerField(max_length=12, null=False, unique=True)
    contraseña = models.CharField(max_length=6, null=False)
 
class colaborador (models.Model):
    id_cargo = models.IntegerField(max_length=12, null=False, unique=True)
    id_persona = models.IntegerField(max_length=12, null=False, unique=True)

class estudiante (models.Model):
    id_usuario = models.IntegerField(max_length=12, null=False, unique=True)
    id_persona = models.IntegerField(max_length=12, null=False, unique=True)

class persona (models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=80)
    apellido_materno = models.CharField(max_length=15)
    apellido_paterno = models.CharField(max_length= 15)
    correo = models.CharField(max_length=30, null=False, unique=True)
    fecha_nacimiento = models.DateField(max_length=30)
    rol = models.CharField(max_length= 30)
    rut = models.IntegerField(max_length= 10, null=False, unique=True)
    telefono = models.IntegerField(max_length=15, null=False, unique=True)

class curso (models.Model):
    nombre_curso = models.CharField(max_length=30, null=False, unique=True)
    lista_alumno = models.IntegerField(max_length=30)
    
