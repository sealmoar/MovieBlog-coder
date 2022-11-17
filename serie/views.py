from datetime import datetime
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.forms.models import model_to_dict
from django.shortcuts import render, get_object_or_404, redirect

from serie.forms import SerieForm
from serie.models import Serie
from serie.forms import CommentForm
from serie.models import Comment

from django.core.exceptions import ValidationError
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class SerieListView(ListView):
    model = Serie
    paginate_by = 3


class SerieDetailView(DetailView):
    model = Serie
    template_name = "serie/serie_detail.html"
    fields = ["name", "category", "seasons", "rate", "review", "image"]

    def get(self, request, pk):
        serie = Serie.objects.get(id=pk)
        comments = Comment.objects.filter(serie=serie).order_by("-updated_at")
        comment_form = CommentForm()
        context = {
            "serie": serie,
            "comments": comments,
            "comment_form": comment_form,
        }
        return render(request, self.template_name, context)

class SerieCreateView(CreateView):
    model = Serie
    success_url = reverse_lazy("serie:serie-list")

    form_class = SerieForm
    # fields = ["name", "category", "description"]

    def form_valid(self, form):
        """Filter to avoid duplicate series"""
        data = form.cleaned_data
        form.instance.owner = self.request.user
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
    fields = ["name", "category", "seasons", "rate", "review", "image"]

    def get_success_url(self):
        serie_id = self.kwargs["pk"]
        return reverse_lazy("serie:serie-detail", kwargs={"pk": serie_id})


class SerieDeleteView(DeleteView):
    model = Serie
    success_url = reverse_lazy("serie:serie-list")

class CommentCreateView(LoginRequiredMixin, CreateView):
   def post(self, request, pk):
        serie = get_object_or_404(Serie, id=pk)
        comment = Comment(
            text=request.POST["comment_text"], owner=request.user, serie=serie
        )
        comment.save()
        return redirect(reverse("serie:serie-detail", kwargs={"pk": pk}))


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment

    def get_success_url(self):
        serie = self.object.serie
        return reverse("serie:serie-detail", kwargs={"pk": serie.id})