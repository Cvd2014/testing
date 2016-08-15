from django.db import models
from django.utils import timezone
# Create your models here.

class Message(models.Model):
    subject = models.CharField(max_length=200)
    email = models.EmailField()
    message=models.TextField()
    sender=models.CharField(max_length=200)
    datetime=models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.email

    class Meta:
        ordering = ['-datetime']


