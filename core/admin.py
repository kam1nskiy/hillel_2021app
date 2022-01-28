from django.contrib import admin
from .models import Like, Post
# from core import models

# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     pass


# @admin.register(Like)
# class PostAdmin(admin.ModelAdmin):
#     pass

class LikeInline(admin.TabularInline):
    model = Like
    fk_name = 'post'


class PostAdmin(admin.ModelAdmin):
    inlines = [
        LikeInline,
    ]
    list_display = 'title', 'user', 'created_at'
    prepopulated_fields = {'slug': ('title',),}    



# class PostAdmin(admin.ModelAdmin):
#     inlines = [
#         LikeInline,
#     ]


#     list_display = 'title', 'user', 'created_at'
#     prepopulated_fields = {'slug': ('title',),}


admin.site.register(Post,PostAdmin)


# Register your models here.
