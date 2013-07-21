from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.views.generic import View

from .forms import PostForm


def home(request):
    template = 'home.html'
    context = {}
    return render_to_response(template,
                              RequestContext(request, context))


class AddPostView(View):

    def post(self, request, *args, **kwargs):
        form_data = request.POST.copy()

        form = PostForm(form_data, request.FILES)
        if form.is_valid():
            form.save()

        return HttpResponseRedirect(reverse('home'))
