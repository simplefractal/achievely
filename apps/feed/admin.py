# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    raw_id_fields = ('user',)
    fields = ('user', 'note', 'image', 'video_url')
    list_display = ('user', 'note', 'image', 'video_url', 'date_added')
    search_fields = ['note']


admin.site.register(Post, PostAdmin)
