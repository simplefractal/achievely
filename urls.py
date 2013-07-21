from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

from feed.views import AddPostView


urlpatterns = patterns('',
    url(r'^$', 'feed.views.home', name='home'),
    url(r'^add_post/$', AddPostView.as_view(), name='add_post'),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)
