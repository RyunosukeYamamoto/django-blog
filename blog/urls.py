from django.contrib import admin
from django.urls import path, include
from articles.views import ArticleListView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", ArticleListView.as_view(), name="home"),
    path("articles/", include("articles.urls")),
]
