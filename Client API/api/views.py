from .models import Client
from .serializer import ClientSerializer
from rest_framework import viewsets


class ClientModelViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
