from django.urls import path
from .views import (
    index,
    view_articles,
    view_news
)

app_name = "content"

urlpatterns = [
    path('', index, name="index"),
    path('articles/', view_articles, name="view_articles"),
    path('news/', view_news, name="view_news")
]