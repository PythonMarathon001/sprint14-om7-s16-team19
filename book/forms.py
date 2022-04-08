from django import forms
from django.core.exceptions import ValidationError

from author.models import Author
from book.models import Book


class BookForm(forms.ModelForm):
    # Для випадаючого списку:
    # def __init__(self, *args, **kwargs):
    #     super.__init__(self, *args, **kwargs)
    #     self.fields['dropwown_field'].empty_label = '--choose one of--'
    class Meta:
        model = Book
        fields = ["name", "description", "count", "authors"]
        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-input'}),
            "description": forms.Textarea(attrs={'cols': 80, 'rows': 4}),
        }
