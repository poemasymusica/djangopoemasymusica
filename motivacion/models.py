from django.db import models
import datetime

class Poemo(models.Model):
    escritor = models.CharField(max_length=50)
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=450)
    poemo_text = models.CharField(max_length=5000)
    img = models.ImageField(upload_to='motivacion/img')
    fecha = models.DateField(datetime.date.today)
    
    def __str__(self):
        return self.titulo
    

