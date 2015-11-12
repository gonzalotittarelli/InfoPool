from django.db import models


class Persona(models.Model):
    """Clase que modela a una persona, la cual puede ser administrador o viajero"""

    usuario = models.CharField(max_length=200)
    clave = models.CharField(max_length=200)




class Administrador(Persona):
    """ Clase que modela a un Administrador del sistema."""
    pass




class Viajero(Persona):
    """ Clase que modela a un Viajero del sistema, el mismo debe registrarse presentando los datos pertinentes. 

    Tendra un estado para representar si esta activo o bloqueado.

    Tambien posee colecciones de recorridos que publica el mismo, asi como los mensajes enviados y recibidos y sus calificaciones.

    """

    nombres = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    telefono = models.CharField(max_length=100)
    mail = models.EmailField(max_length=254)
    foto = models.ImageField(max_length=100)
    bloqueado = models.BooleanField(default=False)
    recorridos = models.ManyToManyField(Recorrido)




class Evento(models.Model):
    """ Clase que modela a un Evento del sistema.

    El mismo sera dado de alta unicamente por un administrador.

    Tendra un nombre, latitud y longitud para su ubicacion, la fecha del evento y los recorridos asociados al mismo.
    """

    nombre = models.CharField(max_length=200)
    direccion = models.TextField(max_length=200)
    fecha = models.DateField()
    latitud = models.DecimalField(max_digits=10, decimal_places=6)
    longitud = models.DecimalField(max_digits=10, decimal_places=6)



class Recorrido(models.Model):
    """ Clase que modela a un Recorrido del sistema.

    El mismo tendra los asientos disponibles, la ruta para trazar el recorrido en el mapa (sera un string que traza la ruta en el mapa desde el origen
    hasta el destino, con sus puntos si es que los hay), una fecha del recorrido que es la fecha en la que se hara el recorrido (puntual), los dias del 
    recorrido (Lunes, Martes, etc), y el tipo de recorrido (Puntual, Periodico o Diario).

    Tambien se contara con una fecha de publicacion del recorrido, los viajeros que participan del mismo, el conductor, la hora de regreso y partida,
    y si esta asociado o no a un evento.

    Una cuestion importante es que solo usuarios conductores pueden dar de alta recorridos. Es decir, no hacemos distincion entre conductor pasajero
    o ambos, para simplificar la cuestion.
    """

    TIPO_DIARIO = 'd'
    TIPO_PERIODICO = 'pe'
    TIPO_PUNTUAL = 'pu'
    OPCIONES_TIPO = (
        (TIPO_DIARIO, 'diario'),
        (TIPO_PERIODICO, 'periodico'),
        (TIPO_PUNTUAL, 'puntual'),
    )
    pasajeros = models.ManyToManyField(Viajero)
    conductor = models.ForeignKey(Viajero, related_name='conductor')
    tipo = models.CharField(max_length=3,choices=OPCIONES_TIPO)
    fecha_publicacion = models.DateField(auto_now_add=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True)
    hora_partida = models.TimeField()
    hora_regreso = models.TimeField(null=True)
    direccion_destino = models.TextField(max_length=200)
    direccion_origen = models.TextField(max_length=200)
    asientos_disponibles = models.IntegerField(default=1)
    evento = models.ForeignKey(Evento, null=True)
    ruta = models.TextField(max_length=300)




class Denuncia(models.Model):
    """Clase que modela a una Denuncia de un usuario hacia otro a partir del recorrido realizado."""

    descripcion = models.TextField(max_length=300)
    denunciante = models.ForeignKey(Viajero, related_name='denunciante')
    denunciado = models.ForeignKey(Viajero, related_name='denunciado')




class Peticion(models.Model):
    """ Clase que modela a una Peticion del sistema.

    La misma es realizada por un viajero para un recorrido y posee un estado (confirmada-rechazada-pendiente) en funcion de si fue atendida, 
    y si lo fue, si fue cancelada o aceptada.

    La fecha representa la fecha en que se realizo la peticion.

    """

    ESTADO_PENDIENTE = 'p'
    ESTADO_ACEPTADA = 'a'
    ESTADO_RECHAZADA = 'r'
    ESTADOS = (
        (ESTADO_PENDIENTE, 'pendiente'),
        (ESTADO_ACEPTADA, 'aceptada'),
        (ESTADO_RECHAZADA, 'rechazada'),
    )


    fecha = models.DateField(auto_now_add=True)
    estado = models.CharField(max_length=2, choices=ESTADOS, default=ESTADO_PENDIENTE)
    recorrido = models.ForeignKey(Recorrido)
    participante = models.ForeignKey(Viajero, related_name='participante')




class Calificacion(models.Model):
    """Clase que modela a una Calificacion realizada por un viajero hacia otro para un recorrido en particular.

    Se registra la fecha y el tipo que representaria si es positiva o negativa.

    """

    fecha = models.DateField(auto_now_add=True)
    tipo = models.BooleanField(default=False)
    viajero_calificado = models.ForeignKey(Viajero, related_name='viajero_calificado')
    viajero_calificador = models.ForeignKey(Viajero, related_name='viajero_calificador')
    recorrido_calificado = models.ForeignKey(Recorrido)




class Mensaje(models.Model):
    """ Clase que modela a un Mensaje del sistema.
    El mismo tendra un destinatario y un remitente , asi como el asunto y el cuerpo. 

    Sera utilizado para la comunicacion entre los usuarios del sistema

    """

    asunto = models.TextField(max_length=300)
    cuerpo = models.TextField(max_length=300)
    fecha = models.DateField(auto_now_add=True)
    hora = models.TimeField(auto_now_add=True)
    destinatario = models.ForeignKey(Viajero, related_name='destinatario')
    remitente = models.ForeignKey(Viajero, related_name='remitente')
