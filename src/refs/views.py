from multiprocessing import context
import select
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.views import generic

from . import models


# Create your views here.
#authors
class AuthorList(generic.ListView):
    model = models.Author


class AuthorDetail(generic.DetailView):
    model = models.Author


class AuthorCreate(generic.CreateView):
    model = models.Author
    fields = ['name', 'series', 'description']


class AuthorUpdate(generic.UpdateView):
    model = models.Author
    fields = ['name', 'series', 'description']


class AuthorDelete(generic.DeleteView):
    model = models.Author
    success_url = "/author-list/"

#Genre
class GenreList(generic.ListView):
    model = models.Genre


class GenreDetail(generic.DetailView):
    model = models.Genre


class GenreCreate(generic.CreateView):
    model = models.Genre
    fields = ['name', 'description']


class GenreUpdate(generic.UpdateView):
    model = models.Genre
    fields = ['name', 'description']


class GenreDelete(generic.DeleteView):
    model = models.Genre
    success_url = "/genre-list/"

#series
class SeriesList(generic.ListView):
    model = models.Series


class SeriesDetail(generic.DetailView):
    model = models.Series


class SeriesCreate(generic.CreateView):
    model = models.Series
    fields = ['name', 'description']


class SeriesUpdate(generic.UpdateView):
    model = models.Series
    fields = ['name', 'description']


class SeriesDelete(generic.DeleteView):
    model = models.Series
    success_url = "/series-list/"

#publishers
class PublisherList(generic.ListView):
    model = models.Publisher


class PublisherDetail(generic.DetailView):
    model = models.Publisher


class PublisherCreate(generic.CreateView):
    model = models.Publisher
    fields = ['name', 'description']


class PublisherUpdate(generic.UpdateView):
    model = models.Publisher
    fields = ['name', 'description']


class PublisherDelete(generic.DeleteView):
    model = models.Publisher
    success_url = "/publisher-list/"
