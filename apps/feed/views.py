from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.views.generic import TemplateView

from .forms import PostForm


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        return {
            'form': PostForm(),
        }

    def post(self, request, *args, **kwargs):
        form_data = request.POST.copy()

        form = PostForm(form_data, request.FILES)
        if form.is_valid():
            form.save()

        return self.get(request, *args, **kwargs)
