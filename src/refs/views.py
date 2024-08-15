from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models


# Create your views here.
#authors
class AuthorList(generic.ListView):
    model = models.Author


class AuthorDetail(generic.DetailView):
    model = models.Author


class AuthorCreate(LoginRequiredMixin, generic.CreateView):
    model = models.Author
    fields = ['name', 'series', 'description']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["headline"] = 'Добавление нового автора'
        return context


class AuthorUpdate(LoginRequiredMixin, generic.UpdateView):
    model = models.Author
    fields = ['name', 'series', 'description']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["headline"] = 'Редактирование автора'
        return context


class AuthorDelete(LoginRequiredMixin, generic.DeleteView):
    model = models.Author
    success_url = reverse_lazy("references:author-list")
#Genre
class GenreList(generic.ListView):
    model = models.Genre


class GenreDetail(generic.DetailView):
    model = models.Genre


class GenreCreate(LoginRequiredMixin, generic.CreateView):
    model = models.Genre
    fields = ['name', 'description']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["headline"] = 'Добавление жанра'
        return context


class GenreUpdate(LoginRequiredMixin, generic.UpdateView):
    model = models.Genre
    fields = ['name', 'description']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["headline"] = 'Редактирование жанра'
        return context


class GenreDelete(LoginRequiredMixin, generic.DeleteView):
    model = models.Genre
    success_url = reverse_lazy("references:genre-list")

#series
class SeriesList(generic.ListView):
    model = models.Series


class SeriesDetail(generic.DetailView):
    model = models.Series


class SeriesCreate(LoginRequiredMixin, generic.CreateView):
    model = models.Series
    fields = ['name', 'description']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["headline"] = 'Добавление серии'
        return context


class SeriesUpdate(LoginRequiredMixin, generic.UpdateView):
    model = models.Series
    fields = ['name', 'description']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["headline"] = 'Редактирование серии'
        return context


class SeriesDelete(LoginRequiredMixin, generic.DeleteView):
    model = models.Series
    success_url = reverse_lazy("references:series-list")

#publishers
class PublisherList(generic.ListView):
    model = models.Publisher


class PublisherDetail(generic.DetailView):
    model = models.Publisher


class PublisherCreate(LoginRequiredMixin, generic.CreateView):
    model = models.Publisher
    fields = ['name', 'description']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["headline"] = 'Добавление издательства'
        return context


class PublisherUpdate(LoginRequiredMixin, generic.UpdateView):
    model = models.Publisher
    fields = ['name', 'description']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["headline"] = 'Редактирование издательства'
        return context


class PublisherDelete(LoginRequiredMixin, generic.DeleteView):
    model = models.Publisher
    success_url = reverse_lazy("references:publisher-list")
