from django import forms
from .models import Articles
from datetime import datetime


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = ["title", "content"]

    def save(self, *args, **kwargs):
        obj = super().save(commit=False)
        obj.create_at = datetime.now()
        obj.update_at = datetime.now()
        obj.save()
        return obj
