from django.db import models


class Articles(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=10000)
    create_at = models.DateTimeField()
    update_at = models.DateTimeField()

    class Meta:
        db_table = "articles"
