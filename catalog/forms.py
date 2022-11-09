from socket import fromshare
from django import forms
from django.forms import CharField, IntegerField, TextInput

class MovieForm(forms.Form):
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
    calif = forms.CharField(
        label = "Movie's calification",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "movie-calif",
                "placeholder": "Movie's calification",
                "required": "True",
            }
        ),
    )

class SerieForm(forms.Form):
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
    season = forms.CharField(
        label = "serie's season",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "serie-season",
                "placeholder": "serie's season",
                "required": "True",
            }
        ),
    )