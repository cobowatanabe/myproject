from django import forms
from .models import Myapp

class SearchForm(forms.Form):
    myapp = forms.ModelChoiceField(
        queryset=Myapp.objects, label='ステータス', required=False)

    