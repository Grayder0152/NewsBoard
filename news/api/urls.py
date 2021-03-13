from django.urls import path, include
from .api_views import NewsBoardAPIView, ArticleAPIView, CommentsAPIView, CommentAPIView, Upvote


urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('news-board/', NewsBoardAPIView.as_view()),
    path('article/<str:link>', ArticleAPIView.as_view()),
    path('article/<str:link>/comments', CommentsAPIView.as_view()),
    path('article/<str:link>/comment/<int:id>', CommentAPIView.as_view()),
    path('article/<str:link>/upvote', Upvote.as_view())
]
