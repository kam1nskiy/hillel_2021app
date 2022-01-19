from email.policy import default
from operator import mod
from turtle import title
from django.db import models
from django.conf import settings

# class Post(models.Model):
#     title = models.CharField(max_length=100, null = False, blank=False)
#     content = models.TextField(null = False, blank=False)
#     image = models.CharField(max_length=255, null = False)
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=False, on_delete=models.SET_NULL)


#     created_at = models.DateTimeField(auto_now_add = True)
#     updated_at = models.DateTimeField(auto_now = True)

#     def __str__(self) -> str:
#         return f"{self.title}"




# class Like(models.Model):
#     post = models.ForeignKey("Post", null = False, blank = False, on_delete = models.CASCADE)
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, null = False, blank = False, on_delete = models.CASCADE)
#     status = models.BooleanField(null = True, blank = True)


#     created_at = models.DateTimeField(auto_now_add = True)
#     updated_at = models.DateTimeField(auto_now = True)
#  Create your models here.


class TimeStampMixin(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Post(TimeStampMixin):
    title = models.CharField(max_length=100, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    image = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=False, on_delete=models.SET_NULL)


    def __str__(self) -> str:
        return f"{self.title}"



class Like(TimeStampMixin):
    post = models.ForeignKey("Post", null=False, blank=False, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, blank=False, on_delete=models.CASCADE)
    status = models.BooleanField(null=True, blank=True)
