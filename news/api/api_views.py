from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView, UpdateAPIView
from rest_framework.response import Response

from .serializers import ArticleSerializers, CommentSerializers
from ..models import Article, Comment


def get_article_id(request, **kwargs):
    article = Article.objects.get(link=kwargs.get('link'))
    request.data['article'] = str(article.id)
    return request


class BaseArticleAPI:
    serializer_class = ArticleSerializers
    queryset = Article.objects.all()


class NewsBoardAPIView(BaseArticleAPI, ListCreateAPIView):
    pass


class ArticleAPIView(BaseArticleAPI, RetrieveUpdateDestroyAPIView):
    lookup_field = 'link'


class BaseCommentAPI:
    serializer_class = CommentSerializers
    queryset = Comment.objects.all()


class CommentsAPIView(BaseCommentAPI, ListCreateAPIView):
    lookup_url_kwarg = 'article'

    def list(self, request, *args, **kwargs):
        article = Article.objects.get(link=kwargs.get('link'))
        queryset = Comment.objects.filter(article=article)
        serializer = CommentSerializers(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        return super().create(get_article_id(request, **kwargs), *args, **kwargs)


class CommentAPIView(BaseCommentAPI, RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        return super().update(get_article_id(request, **kwargs), *args, **kwargs)


class Upvote(BaseArticleAPI, ListCreateAPIView):
    lookup_field = 'link'

    def list(self, request, *args, **kwargs):
        article = Article.objects.get(link=kwargs.get('link'))
        article.amount_upvotes += 1
        article.save()
        serializer = self.get_serializer(article)
        return Response(serializer.data)
