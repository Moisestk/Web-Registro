from django.db import models
from django.contrib.auth.models import User


class Tipo (models.Model):
    tipo_personal = models.CharField(max_length=30)
    
    def __str__(self):
        return self.tipo_personal

class Personal (models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    nombre = models.TextField(null=True)
    apellido = models.TextField(null=True)
    cedula = models.TextField(null=True)
    fecha = models.DateField(null=True)
    salario = models.TextField()

    def __str__(self):
       return self.nombre
      
