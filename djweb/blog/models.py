from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Posts(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

