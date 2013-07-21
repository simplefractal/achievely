from django.forms import ModelForm, Textarea
from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('user', 'note', 'image', 'video_url')
        widgets = {
            'note': Textarea(attrs={'cols': 80, 'rows': 3}),
        }
