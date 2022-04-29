from datetime import date
from django.db import models

class Article(models.Model):
    name=models.CharField(max_length=100)
    text=models.TextField(max_length=1000)
    date=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("Статья")
        verbose_name_plural = ("Статьи")

    def __str__(self):
        return self.name

