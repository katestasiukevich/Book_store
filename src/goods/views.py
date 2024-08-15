from typing import Any
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic as generic_views
from . import models, forms


# Create your views here.
class BookList(generic_views.ListView):
    model = models.Book


class BookCreate(LoginRequiredMixin, generic_views.CreateView):
    model = models.Book
    login_url = reverse_lazy("accounts:login")
    fields = [
        "title",
        "author",
        "series",
        "genre",
        "publisher",
        "cover",
        "description",
        "price",
    ]
    form = forms.BookCreateForm

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["headline"] = 'Добавление нового товара "Книга"'
        return context


class BookDetail(generic_views.DetailView):
    model = models.Book


class BookUpdate(LoginRequiredMixin, generic_views.UpdateView):
    model = models.Book
    fields = [
        "title",
        "author",
        "series",
        "genre",
        "publisher",
        "cover",
        "description",
        "price",
    ]

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["headline"] = 'Редактирование товара "Книга"'
        return context


class BookDelete(LoginRequiredMixin, generic_views.DeleteView):
    model = models.Book
    success_url = reverse_lazy("goods:book-list")


def contact_form(request):
    if request.method == "GET":
        form = forms.ContactForm()
        context = {"form": form}
        return render(request, template_name="goods/contact_form.html", context=context)
    if request.method == "POST":
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            pass #send_email_to_admin(data)
        else:
            context = {"form": form}
            return render(request, template_name="goods/contact_form.html", context=context)
        return HttpResponseRedirect(reverse_lazy("goods:message-sent"))
    
def message_sent(request):
    return render(request, template_name="goods/message-sent.html")
