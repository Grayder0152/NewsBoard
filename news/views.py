from django.views.generic import ListView
from .models import Article


class NewsBoard(ListView):
    model = Article
    queryset = Article.objects.all()
    template_name = "news/newsboard.html"
