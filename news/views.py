from django.views.generic import ListView, DetailView
from django.shortcuts import render

from .models import Article, Comment


class NewsBoardView(ListView):
    model = Article
    queryset = Article.objects.all()
    template_name = "news/index.html"


class ArticleDerailView(DetailView):

    def get(self, request, *args, **kwargs):
        article = Article.objects.get(id=kwargs.get('id'))
        comments = Comment.objects.filter(article=article)
        context = {
            'article': article,
            'comments':comments
        }
        return render(request, 'news/article.html', context)
