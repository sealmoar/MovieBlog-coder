from django import forms
from ckeditor.widgets import CKEditorWidget

from serie.models import Serie

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
                "placeholder": "Series's calification",
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
    image = forms.ImageField()
    class Meta:
        model = Serie
        fields = ["name", "category", "seasons", "rate", "review", "image"]

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
