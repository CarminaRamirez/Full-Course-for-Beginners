from django.shortcuts import render, get_object_or_404
from django.urls import reverse
# Create your views here.

from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    ListView,
    DeleteView
)

from .forms import ArticleForm
from .models import article

class ArticleCreateView(CreateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleForm
    queryset = article.objects.all()
    #success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    #def get_success_url(self):
    #    return '/'

class ArticleListView(ListView):
    template_name = 'articles/article_list.html'
    queryset = article.objects.all() #<blog>/<modelname>_list.html

class ArticleDetailView(DetailView):
    template_name = 'articles/article_detail.html'
    #queryset = article.objects.all()

    def get_object(self):
        id_= self.kwargs.get("id")
        return get_object_or_404(article, id=id_)

class ArticleUpdateView(UpdateView):    #no funciona cuando queres guardar el cambio, ver
    template_name = 'articles/article_create.html'
    form_class = ArticleForm
    queryset = article.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)

    def get_object(self):
        id_= self.kwargs.get("id")
        return get_object_or_404(article, id=id_)

class ArticleDeleteView(DeleteView):
    template_name = 'articles/article_delete.html'
    #queryset = article.objects.all()
    #success_url = '/blog/'

    def get_object(self):
        id_= self.kwargs.get("id")
        return get_object_or_404(article, id=id_)

    def get_success_url(self):
        return reverse('articles:article-list')