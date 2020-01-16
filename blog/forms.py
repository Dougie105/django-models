from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'author',
            'body',
        ]

class RawPostForm(forms.Form):
    title = forms.CharField()
    author = forms.CharField()
    description = forms.CharField()