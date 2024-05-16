from django.views import generic
from .models import Myapp
from .forms import SearchForm

class IndexView(generic.ListView):
    model=Myapp
    