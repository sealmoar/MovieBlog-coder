# Create your models here.
from django.db import models
from ckeditor.fields import RichTextField

class Movie(models.Model):
    name = models.CharField(max_length=35)
    category = models.CharField(max_length=50)
    rate = models.IntegerField()
    review = RichTextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #img = models.ImageField(Upload_to='img') --> PREGUNTAR
        
    def __str__(self):
        return f"{self.name} | {self.category} | {self.rate}"

class Serie(models.Model):
    name = models.CharField(max_length=35)
    category = models.CharField(max_length=50)
    seasons = models.IntegerField()
    rate = models.IntegerField()
    review = RichTextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #img = models.ImageField(Upload_to='img') --> PREGUNTAR
        
    def __str__(self):
        return f"{self.name} | {self.category} | {self.seasons}"
# Create your models here.
