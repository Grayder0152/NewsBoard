from django.urls import path
from .views import NewsBoard

urlpatterns = [
    path('', NewsBoard.as_view())
]
