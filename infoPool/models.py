from django.db import models
from abc import ABCMeta, abstractmethod
from django.utils import timezone

class Persona(models.Model):
    usuario = models.CharField(max_length=200)
    clave = models.CharField(max_length=200)

class Administrador(Persona):
    pass

class Viajero(Persona):
    nombres = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    telefono = models.BigIntegerField(default=0)
    mail = models.EmailField(max_length=254)
    foto = models.ImageField(max_length=100)
    bloqueado = models.BooleanField(default=False)

class Evento(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.TextField(max_length=200)
    fecha = models.DateField(auto_now=True)
    latitud = models.DecimalField(max_digits=10, decimal_places=6)
    longitud = models.DecimalField(max_digits=10, decimal_places=6)    

    def __str__(self):
        return self.nombre


class Recorrido(models.Model):
    REGISTRO_CONDUCTOR = 'C'
    REGISTRO_PASAJERO = 'P'
    REGISTRO_AMBOS = 'A'
    OPCIONES_REGISTRO = (
        (REGISTRO_CONDUCTOR, 'Conductor'),
        (REGISTRO_PASAJERO, 'Pasajero'),
        (REGISTRO_AMBOS, 'Ambos'),
    )
    TIPO_DIARIO = 'D'
    TIPO_PERIODICO = 'PE'
    TIPO_PUNTUAL = 'PU'
    OPCIONES_TIPO = (
        (TIPO_DIARIO, 'Diario'),
        (TIPO_PERIODICO, 'Periodico'),
        (TIPO_PUNTUAL, 'Puntual'),
    )
    pasajeros = models.ManyToManyField(Viajero)
    conductor = models.ForeignKey(Viajero, related_name='conductor')
    condicion = models.CharField(max_length=2, choices=OPCIONES_REGISTRO)
    tipo = models.CharField(max_length=3,choices=OPCIONES_TIPO)
    fecha_publicacion = models.DateField(auto_now=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True)
    hora_partida = models.TimeField()
    hora_regreso = models.TimeField()
    direccion_destino = models.TextField(max_length=200)
    direccion_origen = models.TextField(max_length=200)
    origen_latitud = models.DecimalField(max_digits=10, decimal_places=6)
    origen_longitud = models.DecimalField(max_digits=10, decimal_places=6)
    destino_latitud = models.DecimalField(max_digits=10, decimal_places=6)
    destino_longitud = models.DecimalField(max_digits=10, decimal_places=6)
    asientos_disponibles = models.IntegerField(default=1)
    evento = models.ForeignKey(Evento, null=True)
    ruta = models.TextField(max_length=300)

class Denuncia(models.Model):
    descripcion = models.TextField(max_length=300)
    denunciante = models.ForeignKey(Viajero, related_name='denunciante')
    denunciado = models.ForeignKey(Viajero, related_name='denunciado')

class Comentario(models.Model):
    texto = models.TextField(max_length=300)
    autor = models.ForeignKey(Viajero,related_name='autor_comentario')

class Propuesta(models.Model):
    ESTADO_PENDIENTE = 'P'
    ESTADO_ACEPTADA = 'A'
    ESTADO_RECHAZADA = 'R'
    ESTADOS = (
        (ESTADO_PENDIENTE, 'Pendiente'),
        (ESTADO_ACEPTADA, 'Aceptada'),
        (ESTADO_RECHAZADA, 'Rechazada'),
    )
    fecha = models.DateField(default=timezone.now)
    estado = models.CharField(max_length=2, choices=ESTADOS, default=ESTADO_PENDIENTE)
    recorrido = models.ForeignKey(Recorrido)
    participante = models.ForeignKey(Viajero, related_name='participante')

class Calificacion(models.Model):
    fecha = models.DateField(default=timezone.now)
    valor = models.BooleanField(default=False)
    viajero_calificado = models.ForeignKey(Viajero, related_name='viajero_calificado')
    viajero_calificador = models.ForeignKey(Viajero, related_name='viajero_calificador')
    recorrido = models.ForeignKey(Recorrido)

class Mensaje(models.Model):
    asunto = models.TextField(max_length=300)
    cuerpo = models.TextField(max_length=300)
    fecha = models.DateField()
    hora = models.TimeField()
    destinatario = models.ForeignKey(Viajero, related_name='destinatario')
    remitente = models.ForeignKey(Viajero, related_name='remitente')
