from django.urls import path
from .views import ArticleCreateView, ArticleDetailView, ArticleListView, ArticleCreateConfirmView


app_name = "articles"

urlpatterns = [
    path("", ArticleListView.as_view(), name="article_list"),
    path("create/", ArticleCreateView.as_view(), name="article_create"),
    path("confirm/", ArticleCreateConfirmView.as_view(), name="article_confirm"),
    path("<int:pk>/", ArticleDetailView.as_view(), name="article_detail"),
]
