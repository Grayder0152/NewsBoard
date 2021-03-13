from django.urls import path
from .views import NewsBoardView, ArticleDerailView, create

urlpatterns = [
    path("", NewsBoardView.as_view(), name="index"),
    path("article/<int:id>", ArticleDerailView.as_view(), name="article"),
    path("create/", create, name="create"),
]
