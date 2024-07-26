from typing import Any
from django.shortcuts import render
from django.views import generic as generic_views
from . import models


# Create your views here.
class BookList(generic_views.ListView):
    model = models.Book


class BookCreate(generic_views.CreateView):
    model = models.Book
    fields = ["title", "author", "series", "genre", "publisher", "cover", "price"]
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["headline"] = 'Добавление нового товара "Книга"'
        return context

class BookDetail(generic_views.DetailView):
    model = models.Book


class BookUpdate(generic_views.UpdateView):
    model = models.Book
    fields = ["title", "author", "series", "genre", "publisher", "cover", "price"]

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["headline"] = 'Редактирование товара "Книга"'
        return context


class BookDelete(generic_views.DeleteView):
    model = models.Book
    success_url = "/book-list/"
