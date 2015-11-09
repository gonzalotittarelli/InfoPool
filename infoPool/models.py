from django.db import models
from abc import ABCMeta, abstractmethod

class Persona(models.Model):
    nombre_usuario=models.CharField(max_length=200)
    clave=models.CharField(max_length=200)

class Administrador(Persona):
    pass

class Viajero(Persona):
    nombres=models.CharField(max_length=200)
    apellido=models.CharField(max_length=200)
    telefono=models.BigIntegerField(default=0)
    mail=models.EmailField(max_length=254)
    foto=models.ImageField(max_length=100)
    bloqueado=models.BooleanField(default=False)

class Evento(models.Model):
    nombre=models.CharField(max_length=200)
    descripcion=models.TextField(max_length=300)
    lugar=models.TextField(max_length=200)
    fecha=models.DateField(auto_now=True)
    def __str__(self):
        return self.nombre

class Recorrido(models.Model):
    OPCIONES_REGISTRO = (
        ('C', 'Conductor'),
        ('P', 'Pasajero'),
        ('A', 'Ambos'),
    )
    OPCIONES_TIPO = (
        ('D', 'Diario'),
	('PE', 'Periodico'),
	('PU', 'Puntual'),
    )
    pasajeros=models.ManyToManyField(Viajero)
    conductor=models.ForeignKey(Viajero,related_name='conductor')
    condicion=models.CharField(max_length=2, choices=OPCIONES_REGISTRO)
    tipo=models.CharField(max_length=3,choices=OPCIONES_TIPO)
    fecha_publicacion=models.DateField(auto_now=True)
    fecha_inicio=models.DateField(auto_now=False)
    fecha_fin=models.DateField(null=True)
    hora_partida=models.DateTimeField(auto_now=False)
    hora_llegada=models.DateTimeField(auto_now=False)
    origen_latitud=models.TextField(max_length=200)
    origen_longitud=models.TextField(max_length=200)
    destino_latitud=models.TextField(max_length=200)
    destino_longitud=models.TextField(max_length=200)
    asientos_disponibles=models.IntegerField(default=1)
    evento = models.ForeignKey(Evento)

class Denuncia(models.Model):
    descripcion=models.TextField(max_length=300)
    denunciante=models.ForeignKey(Viajero,related_name='denunciante')
    denunciado=models.ForeignKey(Viajero,related_name='denunciado')

class Comentario(models.Model):
    texto=models.TextField(max_length=300)
    autor=models.ForeignKey(Viajero,related_name='autor_comentario')

class Propuesta(models.Model):
    ESTADOS = (
        ('P', 'Pendiente'),
  	('A', 'Aceptado'),
	('R', 'Rechazado'),
    )
    estado = models.CharField(max_length=2, choices=ESTADOS,default='P')
    recorrido = models.ForeignKey(Recorrido)
    participante = models.ForeignKey(Viajero,related_name='participante')

class Calificacion(models.Model):
    valor=models.BooleanField(default=False)
    viajero=models.ForeignKey(Viajero)
    recorrido=models.ForeignKey(Recorrido)

class Mensaje(models.Model):
    asunto=models.TextField(max_length=300)
    cuerpo=models.TextField(max_length=300)
    autor=models.ForeignKey(Viajero,related_name='autor')
    remitente=models.ForeignKey(Viajero,related_name='remitente')
