from django.contrib import admin

# from .models import Like, Post
from core import models

# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     pass


# @admin.register(Like)
# class PostAdmin(admin.ModelAdmin):
#     pass


class TabularInlineLike(admin.TabularInline):
    model=models.Like

class PostAdmin(admin.ModelAdmin):
    inlines=[TabularInlineLike]
    list_display = ("title", "user")

admin.site.register(models.Post, PostAdmin)



# Register your models here.
