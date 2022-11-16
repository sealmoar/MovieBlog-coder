from django.shortcuts import render

# Create your views here.
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.forms.models import model_to_dict
from django.shortcuts import render, get_object_or_404, redirect

from catalog.forms import MovieForm, SerieForm
from catalog.models import Movie
from catalog.models import Serie
from catalog.forms import CommentForm
from catalog.models import Comment

from django.core.exceptions import ValidationError
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from catalog.models import Movie, Serie


class MovieListView(ListView):
    model = Movie
    paginate_by = 3
    template_name = "catalog/movie_list.html"


class MovieDetailView(DetailView):
    model = Movie
    fields = ["name", "category", "rate", "review"]


class MovieCreateView(CreateView):
    model = Movie
    success_url = reverse_lazy("catalog:movie-list")

    form_class = MovieForm
    # fields = ["name", "category", "description"]

    def form_valid(self, form):
        """Filter to avoid duplicate movies"""
        data = form.cleaned_data
        actual_objects = Movie.objects.filter(
            name=data["name"], category=data["category"]
        ).count()
        if actual_objects:
            messages.error(
                self.request,
                f"La pelicula {data['name']} - {data['category']} ya está creado",
            )
            form.add_error("name", ValidationError("Acción no válida"))
            return super().form_invalid(form)
        else:
            messages.success(
                self.request,
                f"Serie {data['name']} - {data['category']} creado exitosamente!",
            )
            return super().form_valid(form)


class MovieUpdateView(UpdateView):
    model = Movie
    fields = ["name", "category", "rate", "review"]

    def get_success_url(self):
        movie_id = self.kwargs["pk"]
        return reverse_lazy("catalog:movie-detail", kwargs={"pk": movie_id})


class MovieDeleteView(DeleteView):
    model = Movie
    success_url = reverse_lazy("catalog:movie-list")


class CommentCreateView(LoginRequiredMixin, CreateView):
    def post(self, request, pk):
        movie = get_object_or_404(Movie, id=pk)
        comment = Comment(
            text=request.POST["comment_text"], owner=request.user, movie=movie
        )
        comment.save()
        return redirect(reverse("catalog:movie-detail", kwargs={"pk": pk}))


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment

    def get_success_url(self):
        movie = self.object.movie
        return reverse("catalog:movie-detail", kwargs={"pk": movie.id})

class SerieListView(ListView):
    model = Serie
    paginate_by = 3


class SerieDetailView(DetailView):
    model = Serie
    fields = ["name", "category", "seasons", "rate", "review"]


class SerieCreateView(CreateView):
    model = Serie
    success_url = reverse_lazy("catalog:serie-list")

    form_class = SerieForm
    # fields = ["name", "category", "description"]

    def form_valid(self, form):
        """Filter to avoid duplicate series"""
        data = form.cleaned_data
        actual_objects = Serie.objects.filter(
            name=data["name"], category=data["category"]
        ).count()
        if actual_objects:
            messages.error(
                self.request,
                f"Las serie {data['name']} - {data['category']} ya está creada",
            )
            form.add_error("name", ValidationError("Acción no válida"))
            return super().form_invalid(form)
        else:
            messages.success(
                self.request,
                f"Serie {data['name']} - {data['category']} creada exitosamente!",
            )
            return super().form_valid(form)


class SerieUpdateView(UpdateView):
    model = Serie
    fields = ["name", "category", "seasons", "rate", "review"]

    def get_success_url(self):
        serie_id = self.kwargs["pk"]
        return reverse_lazy("catalog:serie-detail", kwargs={"pk": serie_id})


class SerieDeleteView(DeleteView):
    model = Serie
    success_url = reverse_lazy("catalog:serie-list")

class CommentCreateView(LoginRequiredMixin, CreateView):
    def post(self, request, pk):
        serie = get_object_or_404(Movie, id=pk)
        comment = Comment(
            text=request.POST["comment_text"], owner=request.user, serie=serie
        )
        comment.save()
        return redirect(reverse("catalog:serie-detail", kwargs={"pk": pk}))


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment

    def get_success_url(self):
        serie = self.object.serie
        return reverse("catalog:serie-detail", kwargs={"pk": serie.id})