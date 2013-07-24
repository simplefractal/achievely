from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.views.generic import TemplateView

from .models import Post


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        return {
            'posts': Post.objects.all().order_by('-id')
        }


class SingleFeedPostView(TemplateView):
    template_name = "single_post.html"

    def get_context_data(self, _id, **kwargs):
        return {
            'post': Post.objects.get(id=_id)
        }


home = HomeView.as_view()
single_post = SingleFeedPostView.as_view()
