import datetime
from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.files import ImageField



class Poema(models.Model):
    escritor = models.CharField(max_length=50)
    titulo = CharField(max_length=50)
    descripción = CharField(max_length=250)
    poema_text = models.CharField(max_length=5000)
    img = models.ImageField(upload_to='amor/img')
    fecha = models.DateField(datetime.date.today)
    
    def __str__(self):
        return self.titulo
