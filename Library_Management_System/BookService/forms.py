from pyexpat import model
from statistics import mode
from django import forms
from .models import Book
from django import forms


class BookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields=("title","description",)
        
