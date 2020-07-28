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

from .models import article

class ArticleListView(ListView):
    template_name = 'articles/article_list.html'
    queryset = article.objects.all() #<blog>/<modelname>_list.html

#def article_list_view(request):
#    queryset = Article.objects.all() #list of objects
#    context = {
#        "object_list": queryset
#    }
#    return render(request, "articles/article_list.html", context)