from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView,
    ListCreateAPIView
)
from rest_framework.response import Response

from .serializers import (
    ArticleSerializers,
    CommentSerializers
)
from ..models import Article, Comment


def get_article_id(request, **kwargs):
    """Function for get article id from url"""
    article = Article.objects.get(link=kwargs.get("link"))
    request.data["article"] = str(article.id)
    return request


class BaseArticleAPI:
    """Template settings for class NewsBoardAPIView and ArticleAPIView"""

    serializer_class = ArticleSerializers
    queryset = Article.objects.all()


class NewsBoardAPIView(BaseArticleAPI, ListCreateAPIView):
    """GET/POST methods for list articles"""

    pass


class ArticleAPIView(BaseArticleAPI, RetrieveUpdateDestroyAPIView):
    """DELETE/UPDATE methods for an article"""

    lookup_field = "link"


class BaseCommentAPI:
    """Template settings for class CommentsListAPIView and CommentAPIView"""

    serializer_class = CommentSerializers
    queryset = Comment.objects.all()


class CommentsListAPIView(BaseCommentAPI, ListCreateAPIView):
    """GET/POST methods for list comments an article"""

    lookup_url_kwarg = "article"

    def list(self, request, *args, **kwargs):
        article = Article.objects.get(
            link=kwargs.get("link")
        )
        queryset = Comment.objects.filter(article=article)
        serializer = CommentSerializers(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        return super().create(
            get_article_id(request, **kwargs),
            *args,
            **kwargs
        )


class CommentAPIView(BaseCommentAPI, RetrieveUpdateDestroyAPIView):
    """DELETE/UPDATE methods for comment an article"""

    lookup_field = "id"

    def update(self, request, *args, **kwargs):
        return super().update(
            get_article_id(request, **kwargs),
            *args,
            **kwargs
        )


class Upvote(BaseArticleAPI, ListCreateAPIView):
    """Endpoint to vote for an article"""

    lookup_field = "link"

    def list(self, request, *args, **kwargs):
        article = Article.objects.get(link=kwargs.get("link"))
        article.amount_upvotes += 1
        article.save()
        serializer = self.get_serializer(article)
        return Response(serializer.data)
