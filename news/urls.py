from django.urls import path
from .views import NewsBoardView, ArticleDerailView

urlpatterns = [
    path('', NewsBoardView.as_view(), name='index'),
    path('article/<int:id>', ArticleDerailView.as_view(), name='article')
]
