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


def movie_create(request):
    if request.method == "POST":
        movie_form = MovieForm(request.POST)
        if movie_form.is_valid():
            data = movie_form.cleaned_data
            actual_objects = Movie.objects.filter(
                name=data["name"], category=data["category"]
            ).count()
            print("actual_objects", actual_objects)
            if not actual_objects:
                movie = Movie(
                    name=data["name"],
                    category=data["category"],
                    rate=data["rate"],
                    description=data["review"],
                )
                movie.save()
                messages.success(
                    request,
                    f"Pelicula {data['name']} - {data['category']} creado exitosamente!",
                )
                return render(
                    request=request,
                    context={"movie_list": get_movies(request)},
                    template_name="catalog/movie_list.html",
                )
            else:
                messages.error(
                    request,
                    f"El pelicula {data['name']} - {data['category']} ya está creada",
                )

    movie_form = MovieForm(request.POST)
    context_dict = {"form": movie_form}
    return render(
        request=request, 
        context=context_dict, 
        template_name="catalog/movie_form.html"
    )


def movies(request):
    return render(
        request=request,
        context={"movie_list": get_movies(request)},
        template_name="catalog/movie_list.html",
    )

def movie_detail(request, pk: int):
    return render(
        request=request,
        context={"movie": Movie.objects.get(pk=pk)},
        template_name="movie/movie_detail.html",
    )

def movie_update(request, pk: int):
    movie = Movie.objects.get(pk=pk)

    if request.method == "POST":
        movie_form = MovieForm(request.POST)
        if movie_form.is_valid():
            data = movie_form.cleaned_data
            movie.name = data["name"]
            movie.category = data["category"]
            movie.rate = data["rate"]
            movie.rate = data["review"]
            movie.save()

            return render(
                request=request,
                context={"movie": movie},
                template_name="catalog/movie_detail.html",
            )

    movie_form = MovieForm(model_to_dict(movie))
    context_dict = {
        "movie": movie,
        "form": movie_form,
    }
    return render(
        request=request,
        context=context_dict,
        template_name="catalog/movie_form.html",
    )


def movie_delete(request, pk: int):
    movie = Movie.objects.get(pk=pk)
    if request.method == "POST":
        movie.delete()

        movies = Movie.objects.all()
        context_dict = {"movie_list": movies}
        return render(
            request=request,
            context=context_dict,
            template_name="catalog/movie_list.html",
        )

    context_dict = {
        "movie": movie,
    }
    return render(
        request=request,
        context=context_dict,
        template_name="catalog/movie_confirm_delete.html",
    )


def get_series(request):
    series = Serie.objects.all()
    paginator = Paginator(series, 3)
    page_number = request.GET.get("page")
    return paginator.get_page(page_number)


def series(request):
    return render(
        request=request,
        context={"serie_list": get_series(request)},
        template_name="catalog/serie_list.html",
    )


def serie_create(request):
    if request.method == "POST":
        serie_form = SerieForm(request.POST)
        if serie_form.is_valid():
            data = serie_form.cleaned_data
            actual_objects = Serie.objects.filter(
                name=data["name"], category=data["category"]
            ).count()
            print("actual_objects", actual_objects)
            if not actual_objects:
                serie = Serie(
                    name=data["name"],
                    category=data["category"],
                    seasons=data["seasons"],
                    rate=data["rate"],
                    review=data["review"],
                )
                serie.save()
                messages.success(
                    request,
                    f"Serie {data['name']} - {data['category']} creada exitosamente!",
                )
                return render(
                    request=request,
                    context={"serie_list": get_series(request)},
                    template_name="catalog/serie_list.html",
                )
            else:
                messages.error(
                    request,
                    f"La serie {data['name']} - {data['category']} ya está creada",
                )

    serie_form = SerieForm(request.POST)
    context_dict = {"form": serie_form}
    return render(
        request=request,
        context=context_dict,
        template_name="catalog/serie_form.html",
    )


def serie_detail(request, pk: int):
    return render(
        request=request,
        context={"serie": Serie.objects.get(pk=pk)},
        template_name="catalog/serie_detail.html",
    )


def serie_update(request, pk: int):
    serie = Serie.objects.get(pk=pk)

    if request.method == "POST":
        serie_form = SerieForm(request.POST)
        if serie_form.is_valid():
            data = serie_form.cleaned_data
            serie.name = data["name"]
            serie.category = data["cateory"]
            serie.seasons = data["seasons"]
            serie.rate = data["rate"]
            serie.review = data["review"]
            serie.save()

            return render(
                request=request,
                context={"serie": serie},
                template_name="catalog/serie_detail.html",
            )

    serie_form = SerieForm(model_to_dict(serie))
    context_dict = {
        "serie": serie,
        "form": serie_form,
    }
    return render(
        request=request,
        context=context_dict,
        template_name="catalog/serie_form.html",
    )


def serie_delete(request, pk: int):
    serie = Serie.objects.get(pk=pk)
    if request.method == "POST":
        serie.delete()

        series = Serie.objects.all()
        context_dict = {"serie_list": series}
        return render(
            request=request,
            context=context_dict,
            template_name="catalog/serie_list.html",
        )

    context_dict = {
        "serie": serie,
    }
    return render(
        request=request,
        context=context_dict,
        template_name="catalog/serie_confirm_delete.html",
    )