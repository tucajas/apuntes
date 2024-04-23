from rest_framework import serializers
from apunte.models import Apunte


class ApunteSerializer(serializers.ModelSerializer):
    class Meta:
        model   = Apunte
        fields  = "__all__"
