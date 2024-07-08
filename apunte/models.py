from django.db import models

# Create your models here.
class Apunte (models.Model):
    descripcion =   models.CharField(max_length=600)
    texto       =   models.TextField(max_length=2000)
    
    def __str__(self):
        return str (self.descripcion)