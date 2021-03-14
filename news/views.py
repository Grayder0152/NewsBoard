from django.shortcuts import redirect, HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.shortcuts import render

from .forms import ArticleForm
from .models import Article, Comment


class NewsBoardView(ListView):
    """List with all article"""

    model = Article
    queryset = Article.objects.all()
    paginate_by = 10
    template_name = "news/index.html"


class ArticleDerailView(DetailView):
    """Detail information about article"""

    def get(self, request, *args, **kwargs):
        article = Article.objects.get(id=kwargs.get("id"))
        comments = Comment.objects.filter(article=article)
        context = {
            "article": article,
            "comments": comments
        }
        return render(request, "news/article.html", context)

    def post(self, request, *args, **kwargs):
        Comment.objects.create(
            author_name=request.POST.get('name'),
            content=request.POST.get('comment'),
            article=Article.objects.get(id=kwargs.get('id'))
        )
        return redirect(f'/article/{kwargs.get("id")}')


def create_article(request):
    """Function for create article"""

    if request.method == "POST":
        form = ArticleForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect("index")
    form = ArticleForm()
    context = {"form": form}
    return render(request, "news/create.html", context)


def upvote_article(request, id):
    """Function to upvote the article"""

    article = Article.objects.get(id=id)
    response = HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    print(request.COOKIES)
    if str(id) in request.COOKIES:
        article.amount_upvotes -= 1
        response.delete_cookie(str(id))
    else:
        article.amount_upvotes += 1
        response.set_cookie(str(id), 'voted')
    article.save()
    return response
