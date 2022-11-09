from django.urls import URLPattern, path

from catalog import views


app_name = "catalog"
urlpatterns = [
    path("movies", views.movies, name="movie-list"),
    path("series", views.series, name="serie-list"),
    path("create-movies", views.create_movies, name="movie-add"),
    path("create-series", views.create_series, name="serie-add"),
]
