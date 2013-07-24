# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    raw_id_fields = ('user',)
    fields = ('user', 'note', 'image', 'video')
    list_display = ('user', 'note', 'image', 'video', 'date_added')
    search_fields = ['note']


class CommentAdmin(admin.ModelAdmin):
    raw_id_fields = ('user', 'post')
    fields = ('user', 'post', 'text')
    list_display = ('user', 'post', 'text', 'date_added')
    search_fields = ['text', 'user']


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
