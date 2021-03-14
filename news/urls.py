from django.urls import path
from .views import (
    NewsBoardView,
    ArticleDerailView,
    create_article,
    upvote_article
)

urlpatterns = [
    path("", NewsBoardView.as_view(), name="index"),
    path("article/<int:id>/", ArticleDerailView.as_view(), name="article"),
    path("article/<int:id>/upvote/", upvote_article, name="upvote"),
    path("create/", create_article, name="create")
]
