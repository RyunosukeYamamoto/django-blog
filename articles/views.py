from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.views.generic.edit import CreateView, FormView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Articles
from django.urls import reverse_lazy
from datetime import datetime
from . import forms


class ArticleCreateView(FormView):
    template_name = "article_create.html"
    form_class = forms.ArticleForm


class ArticleCreateConfirmView(View):
    def post(self, request, *args, **kwargs):
        form = forms.ArticleForm(request.POST or None)
        context = {"form": form}
        if "confirm" in request.POST:
            return render(request, "article_confirm.html", context)
        if "back" in request.POST:
            return render(request, "article_create.html", context)
        if "create" in request.POST:
            form.save()
            return redirect("home")
        else:
            # 正常動作ではここは通らない。エラーページへの遷移でも良い
            return redirect("home")


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
