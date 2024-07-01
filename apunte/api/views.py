from rest_framework import generics
from apunte.api.serializers import ApunteSerializer
from apunte.models import Apunte
from rest_framework.permissions import IsAuthenticated

class ApunteList(generics.ListCreateAPIView):
    queryset    =   Apunte.objects.all()
    serializer_class    =   ApunteSerializer

class ApunteDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAuthenticated]
    queryset     = Apunte.objects.all()
    serializer_class    =   ApunteSerializer