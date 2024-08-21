from django.db import models

class Cliente(models.Model):
    dni = models.IntegerField(primary_key=True)
    nya = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    cuil = models.CharField(max_length=20)
    mail = models.EmailField()

class Vehiculo(models.Model):
    patente = models.CharField(max_length=10, primary_key=True)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

class Turno(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    estado = models.BooleanField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
