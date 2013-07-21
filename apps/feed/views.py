from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.views.generic import TemplateView

from .forms import PostForm
from .models import Post


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        return {
            'form': PostForm(),
            'posts': Post.objects.all().order_by('-id')
        }

    def post(self, request, *args, **kwargs):
        form_data = {}
        form_data['user'] = request.user.id
        form_data['note'] = request.POST.get('note')
        form_data['video_url'] = request.POST.get('video_url')

        form = PostForm(form_data, request.FILES)

        if form.is_valid():
            form.save()

        return self.get(request, *args, **kwargs)


class SingleFeedPostView(TemplateView):
    template_name = "single_post.html"

    def get_context_data(self, _id, **kwargs):
        return {
            'post': Post.objects.get(id=_id)
        }


home = HomeView.as_view()
single_post = SingleFeedPostView.as_view()
