from django import forms
from ckeditor.widgets import CKEditorWidget

from catalog.models import Movie, Serie

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

    class Meta:
        model = Movie
        fields = ["name", "category", "rate", "review"]

class SerieForm(forms.ModelForm):
    name = forms.CharField(
        label = "serie's name",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "serie-name",
                "placeholder": "serie's name",
                "required": "True",
            }
        ),
    )
    category = forms.CharField(
        label = "serie's category",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "serie-category",
                "placeholder": "serie's category",
                "required": "True",
            }
        ),
    )
    seasons = forms.IntegerField(
        label = "serie's seasons",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "serie-seasons",
                "placeholder": "number of seasons",
                "required": "True",
            }
        ),
    )
    rate = forms.IntegerField(
        label = "Movie's Rating",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "serie-rate",
                "placeholder": "Movie's calification",
                "required": "True",
            }
        ),
    )
    review = forms.CharField(
        label="Opinión de Serie:",
        required=False,
        widget=CKEditorWidget(
            attrs={
                "class": "serie-review",
                "placeholder": "Escribe tu opnión de la Serie",
                "required": "True",
            }
        ),
    )

    class Meta:
        model = Serie
        fields = ["name", "category", "seasons", "rate", "review"]