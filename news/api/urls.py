from django.urls import path

from .api_views import NewsBoardAPIView, ArticleAPIView, CommentsAPIView, CommentAPIView

urlpatterns = [
    path('news-board/', NewsBoardAPIView.as_view()),
    path('article/<str:link>', ArticleAPIView.as_view()),
    path('article/<str:link>/comments', CommentsAPIView.as_view()),
    path('article/<str:link>/comment/<int:id>', CommentAPIView.as_view())
]
