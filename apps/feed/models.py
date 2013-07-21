# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


def image_file_name(instance, filename):
    filename, ext = filename.split('.')
    code = instance.slug
    filename = "{}.{}".format(code, ext)
    return 'img/post/{}'.format(filename)


class Post(models.Model):
    user = models.ForeignKey('auth.User')
    note = models.CharField(max_length=250)
    slug = models.SlugField(max_length=150, unique=True, blank=True)
    image = models.ImageField(upload_to=image_file_name, blank=True)
    video_url = models.URLField(max_length=400, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.note

    @property
    def user_icon_url(self):
        return u'img/user/{}.jpg'.format(self.user.username)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = User.objects.make_random_password()
        return super(Post, self).save(*args, **kwargs)
