from .models import Variables
from rest_framework import viewsets, permissions
from .serializers import VarSerializer

class VarViewSet(viewsets.ModelViewSet):
    queryset = Variables.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = VarSerializer