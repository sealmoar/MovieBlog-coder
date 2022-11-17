from django import forms
from ckeditor.widgets import CKEditorWidget

from movie.models import Movie

class MovieForm(forms.ModelForm):
    name = forms.CharField(
        label = "Movie's name",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "movie-name",
                "placeholder": "Movie's name",
                "required": "True",
            }
        ),
    )
    category = forms.CharField(
        label = "Movie's category",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "movie-category",
                "placeholder": "Movie's category",
                "required": "True",
            }
        ),
    )
    rate = forms.IntegerField(
        label = "Movie's Rating",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "movie-rate",
                "placeholder": "Movie's calification",
                "required": "True",
            }
        ),
    )
    review = forms.CharField(
        label="Opinión de Pelicula:",
        required=False,
        widget=CKEditorWidget(
            attrs={
                "class": "movie-review",
                "placeholder": "Escribe tu opnión de la Pelicula",
                "required": "True",
            }
        ),
    )

    image = forms.ImageField()
    
    class Meta:
        model = Movie
        fields = ["name", "category", "rate", "review", "image"]

class CommentForm(forms.Form):
    comment_text = forms.CharField(
        label="",
        required=False,
        max_length=500,
        min_length=10,
        strip=True,
        widget=forms.Textarea(
            attrs={
                "class": "comment-text",
                "placeholder": "Ingrese su comentario...",
                "required": "True",
                "max_length": 500,
                "min_length": 10,
                "rows": 2,
                "cols": 10,
                "style":"min-width: 100%",
            }
        ),
    )
