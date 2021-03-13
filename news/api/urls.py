from django.urls import path
from .api_views import (
    NewsBoardAPIView,
    ArticleAPIView,
    CommentsListAPIView,
    CommentAPIView,
    Upvote,
)


urlpatterns = [
    path("news-board/", NewsBoardAPIView.as_view()),
    path("article/<str:link>", ArticleAPIView.as_view()),
    path("article/<str:link>/comments", CommentsListAPIView.as_view()),
    path("article/<str:link>/comment/<int:id>", CommentAPIView.as_view()),
    path("article/<str:link>/upvote", Upvote.as_view()),
]
