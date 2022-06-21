import imp
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title =models.CharField(max_length=200)
    text =models.TextField ()
    author =models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    Created_Date =models.DateTimeField(auto_now_add=True)
    Published_Date =models.DateTimeField(auto_now_add=True)