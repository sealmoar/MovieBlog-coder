from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db import models
from ckeditor.fields import RichTextField

class Serie(models.Model):
    name = models.CharField(max_length=35)
    category = models.CharField(max_length=50)
    seasons = models.IntegerField(null=False, blank=False)
    rate = models.IntegerField(null=False, blank=False)
    review = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to='serie', null =True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    comments = models.ManyToManyField(
        User, through="Comment", related_name="serie_comments"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #img = models.ImageField(Upload_to='img') --> PREGUNTAR
    
    class Meta:
        unique_together = (
            "name",
            "category",
        )
        ordering = ["-created_at"]
    
    
    def __str__(self):
        return f"{self.name} | {self.category} | {self.seasons}"   

class Comment(models.Model):
    text = models.TextField(
        validators=[
            MinLengthValidator(10, "El comentario debe ser mayor de 10 caracteres")
        ]
    )
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, related_name="serie_owner", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} | {self.category} | {self.rate}"