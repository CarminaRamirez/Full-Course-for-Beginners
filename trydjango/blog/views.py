from django.shortcuts import render

# Create your views here.

from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    ListView,
    DeleteView
)

from .models import Article

class ArtivleListView(ListView):
    queryset = Article.objects.all()