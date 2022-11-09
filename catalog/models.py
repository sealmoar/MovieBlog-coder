# Create your models here.
from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=35)
    category = models.CharField(max_length=50)
    calif = models.IntegerField()
    #img = models.ImageField(Upload_to='img') --> PREGUNTAR
        
    def __str__(self) -> str:
        return f"{self.name} | {self.category} | {self.calif}"

class Serie(models.Model):
    name = models.CharField(max_length=35)
    category = models.CharField(max_length=50)
    seasons = models.IntegerField()
    #img = models.ImageField(Upload_to='img') --> PREGUNTAR
        
    def __str__(self) -> str:
        return f"{self.name} | {self.category} | {self.seasons}"
# Create your models here.
