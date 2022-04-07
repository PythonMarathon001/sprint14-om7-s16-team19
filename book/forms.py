from django import forms

from book.models import Book


class AddPostForm(forms.ModelForm):
    # title = forms.CharField(max_length=255)
    # slug = forms.SlugField(max_length=255)

    # Для випадаючого списку:
    # def __init__(self, *args, **kwargs):
    #     super.__init__(self, *args, **kwargs)
    #     self.fields['dropwown_field'].empty_label = '--choose one of--'

    class Meta:
        model = Book
        # fields = "__all__"
        fields = ["name", "description", "count", "authors"]
        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-input'}),
            "description": forms.Textarea(attrs={'cols': 80, 'rows': 4}),
        }
