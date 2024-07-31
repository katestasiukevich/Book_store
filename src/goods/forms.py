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
            "price"
        ]
        widget = {"genre": forms.ModelMultipleChoiceField(queryset=Genre.objects.all())}
