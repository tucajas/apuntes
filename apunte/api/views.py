from rest_framework import generics
from apunte.api.serializers import ApunteSerializer
from apunte.models import Apunte

class ApunteList(generics.ListCreateAPIView):
    queryset    =   Apunte.objects.all()
    serializer_class    =   ApunteSerializer

class ApunteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset     = Apunte.objects.all()
    serializer_class    =   ApunteSerializer