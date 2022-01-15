from operator import mod
from turtle import title
from django.db import models
from django.conf import settings

class Post(models.Model):
    title = models.CharField(max_length=100, null = False)
    content = models.TextField()
    image = models.CharField(max_length=255, null = False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True,on_delete=models.SET_NULL)


    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    

# Create your models here.
