from django.urls import URLPattern, path

from catalog import views


app_name = "catalog"
urlpatterns = [
    path("movies/", views.MovieListView.as_view(), name="movie-list"),
    path("movie/add/", views.MovieCreateView.as_view(), name="movie-add"),
    path("movie/<int:pk>/detail/", views.MovieDetailView.as_view(), name="movie-detail"),
    path("movie/<int:pk>/update/", views.MovieUpdateView.as_view(), name="movie-update"),
    path("movie/<int:pk>/delete/", views.MovieDeleteView.as_view(), name="movie-delete"),
    path("series/", views.SerieListView.as_view(), name="serie-list"),
    path("serie/add/", views.SerieCreateView.as_view(), name="serie-add"),
    path("serie/<int:pk>/detail/", views.SerieDetailView.as_view(), name="serie-detail"),
    path("serie/<int:pk>/update/", views.SerieUpdateView.as_view(), name="serie-update"),
    path("serie/<int:pk>/delete/", views.SerieDeleteView.as_view(), name="serie-delete"),
]
