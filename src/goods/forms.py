from django import forms

from refs.models import Genre
from . import models

class BookCreateForm(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = [         # "__all__"
            "title",
            "cover",
            "author",
            "series",
            "genre",
            "publisher",
            "description",
            "price"
        ]
        widget = {"genre": forms.ModelMultipleChoiceField(queryset=Genre.objects.all())}

class ContactForm(forms.Form):
    name = forms.CharField( max_length=100, min_length=1, required=True, label="Введите ваше имя")
    message = forms.CharField(required=True, label="Оставьте ваше сообщение", widget=forms.Textarea)
