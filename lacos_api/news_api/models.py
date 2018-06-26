from django.db import models


class News(models.Model):
    title = models.CharField(max_length=30)
    text = models.CharField(max_length=132)
    created = models.DateTimeField(auto_now_add=True)
    date_deleted = models.DateTimeField(auto_now_add=False)
