from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import User, Category, Post, PostDetail, Comment


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'username', 'gender')
    list_display_links = ('id', 'first_name', 'last_name')
    ordering = ['id']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    list_display_links = ('id', 'title')
    ordering = ['id']


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'body', 'created_at')
    list_display_links = ('id', 'title', 'body')
    ordering = ['id']


class PostDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'likes', 'dislikes', 'views')
    list_display_links = ('id', 'post')
    ordering = ['id']


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'post', 'text', 'created_at')
    list_display_links = ('id', 'user', 'post')


admin.site.register(User, UserAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(PostDetail, PostDetailAdmin)
admin.site.register(Comment, CommentAdmin)
