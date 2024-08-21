from rest_framework import serializers
from .models import Turno, Cliente, Vehiculo

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = '__all__'

class TurnoSerializer(serializers.ModelSerializer):
    cliente = ClienteSerializer()
    vehiculo = VehiculoSerializer()

    class Meta:
        model = Turno
        fields = '__all__'
