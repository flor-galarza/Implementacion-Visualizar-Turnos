from .serializers import TurnoSerializer
from .models import Turno
from rest_framework import viewsets

class TurnoViewSet(viewsets.ModelViewSet):
    queryset = Turno.objects.all()
    serializer_class = TurnoSerializer

