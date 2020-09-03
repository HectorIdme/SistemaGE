from django.db import models

# Create your models here.

class Asistente(models.Model):
    ApellidoPaterno = models.CharField(max_length=35)
    ApellidoMaterno = models.CharField(max_length=35)
    Nombres = models.CharField(max_length=35)
    DNI = models.CharField(max_length=8)
    SEXOS = (('F', 'Femenino'), ('M', 'Masculino'), ('N', 'No especifica'))
    Sexo = models.CharField(max_length=1, choices=SEXOS, default='M')

    def nombre_completo(self):
        cadena = "{0} {1}, {2}"
        return cadena.format(self.ApellidoPaterno, self.ApellidoMaterno, self.Nombres)

    def __str__(self):
        return self.nombre_completo()


class Evento(models.Model):
    Nombre = models.CharField(max_length=50)
    Tipo = models.CharField(max_length=50)
    Direccion = models.CharField(max_length=100)
    Estado = models.BooleanField(default=True)

    def __str__(self):
        return "{0} => {1}".format(self.Nombre, self.Tipo)


class Inscripcion(models.Model):
    asistente = models.ForeignKey(Asistente, null=False, blank=False, on_delete=models.CASCADE)
    evento = models.ForeignKey(Evento, null=False, blank=False, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        cadena = "{0} => {1}"
        return cadena.format(self.asistente, self.evento.Nombre)
