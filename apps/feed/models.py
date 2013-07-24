# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import post_save

from .listeners import sync_media_s3
from util.thumborz import thumb


def image_file_name(instance, filename):
    filename, ext = filename.split('.')
    code = instance.slug
    filename = "{}.{}".format(code, ext)
    return 'img/post/{}'.format(filename)


def video_file_name(instance, filename):
    filename, ext = filename.split('.')
    code = instance.slug
    filename = "{}.{}".format(code, ext)
    return 'video/post/{}'.format(filename)


class Post(models.Model):
    user = models.ForeignKey('auth.User')
    note = models.CharField(max_length=250)
    slug = models.SlugField(max_length=150, unique=True, blank=True)
    image = models.ImageField(upload_to=image_file_name, blank=True)
    video = models.FileField(upload_to=video_file_name, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.note

    @property
    def user_icon_url(self):
        path = '{}img/user/{}.jpg'.format(
            settings.MEDIA_URL,
            self.user.username)
        return thumb(path, width=50, height=50, unsafe=True)

    @property
    def detail_url(self):
        if settings.LOCAL:
            domain = "http://127.0.0.1:8000"
        else:
            domain = "http://betterme.herokuapp.com"
        return "{}{}".format(domain, reverse('single_post', args=[self.id]))

    @property
    def image_url(self):
        return thumb(self.image, width=600, height=400, fit_in=True, unsafe=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = User.objects.make_random_password()
        return super(Post, self).save(*args, **kwargs)


post_save.connect(sync_media_s3, sender=Post)
