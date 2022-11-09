from django.shortcuts import render

# Create your views here.
from datetime import datetime
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.forms.models import model_to_dict

from catalog.forms import MovieForm, SerieForm
from catalog.models import Movie
from catalog.models import Serie


def get_movies(request):
    movies = Movie.objects.all()
    paginator = Paginator(movies, 3)
    page_number = request.GET.get("page")
    return paginator.get_page(page_number)


def create_movies(request):
    if request.method == "POST":
        movie_form = MovieForm(request.POST)
        if movie_form.is_valid():
            data = movie_form.cleaned_data
            actual_objects = Movie.objects.filter(
                name=data["name"], category=data["category"]
            ).count()
            if actual_objects:
                messages.error(
                    request,
                    f"La pelicula {data['name']} - {data['category']} ya está creada",
                )
            else:
                movie = Movie(name=data["name"], category=data["cateogry"],rate=data["rate"], review=data["review"])
                movie.save()
                messages.success(
                    request,
                    f"Pelicula {data['name']} - {data['category']} creado exitosamente!",
                )

            return render(
                request=request,
                context={"movies": Movie.objects.all()},
                template_name="catalog/movie_list.html",
            )

    movie_form = MovieForm(request.POST)
    context_dict = {"form": movie_form}
    return render(
        request=request, context=context_dict, template_name="catalog/movie_form.html"
    )


def movies(request):
    return render(
        request=request,
        context={"movies": get_movies(request)},
        template_name="catalog/movie_list.html",
    )

def get_series(request):
    series = Serie.objects.all()
    paginator = Paginator(series, 3)
    page_number = request.GET.get("page")
    return paginator.get_page(page_number)


def create_series(request):
    if request.method == "POST":
        serie_form = SerieForm(request.POST)
        if serie_form.is_valid():
            data = serie_form.cleaned_data
            actual_objects = Serie.objects.filter(
                name=data["name"], category=data["category"]
            ).count()
            if actual_objects:
                messages.error(
                    request,
                    f"La serie {data['name']} - {data['category']} ya está creada",
                )
            else:
                serie = Serie(name=data["name"], category=data["cateogry"],seasons=data["seasons"], rate=data["rate"], review=data["review"])
                serie.save()
                messages.success(
                    request,
                    f"Serie {data['name']} - {data['category']} creado exitosamente!",
                )

            return render(
                request=request,
                context={"series": Serie.objects.all()},
                template_name="catalog/serie_list.html",
            )

    serie_form = SerieForm(request.POST)
    context_dict = {"form": serie_form}
    return render(
        request=request, context=context_dict, template_name="catalog/serie_form.html"
    )


def series(request):
    return render(
        request=request,
        context={"series": get_series(request)},
        template_name="catalog/serie_list.html",
    )