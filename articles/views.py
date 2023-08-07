from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Articles
from django.urls import reverse_lazy
from datetime import datetime


class ArticleCreateView(CreateView):
    model = Articles
    template_name = "article_create.html"
    fields = ["title", "content"]

    success_url = reverse_lazy("articles:article_list")

    def form_valid(self, form):
        form.instance.create_at = datetime.now()
        form.instance.update_at = datetime.now()
        return super().form_valid(form)


class ArticleListView(ListView):
    model = Articles
    template_name = "article_list.html"

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.order_by("-update_at")
        return qs


class ArticleDetailView(DetailView):
    model = Articles
    template_name = "article_detail.html"
