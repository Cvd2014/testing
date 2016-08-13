from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


# Create your models here.
class Article(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=400)
    synopsis = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
