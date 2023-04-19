from django.db import models

class Music(models.Model):
    nombre = models.CharField(max_length=50)
    letra = models.CharField(max_length=500)
    img = models.ImageField(upload_to=('musica/img'))
    url = models.URLField(blank=True)

    def __str__(self):
        return self.nombre
    