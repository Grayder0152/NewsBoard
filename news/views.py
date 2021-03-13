from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from .forms import ArticleForm

from .models import Article, Comment


class NewsBoardView(ListView):
    """List with all article"""

    model = Article
    queryset = Article.objects.all()
    template_name = "news/index.html"


class ArticleDerailView(DetailView):
    """Detail information about article"""

    def get(self, request, *args, **kwargs):
        article = Article.objects.get(id=kwargs.get("id"))
        comments = Comment.objects.filter(article=article)
        context = {"article": article, "comments": comments}
        return render(request, "news/article.html", context)


def create(request):
    """Function for create article"""

    error = ""
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
        else:
            error = "Invalid input"
    form = ArticleForm()
    context = {"form": form, "error": error}
    return render(request, "news/create.html", context)
