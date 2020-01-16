from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from .forms import PostForm


def HomePageView(request, *args, **kwargs):
    my_context = {
        'my_list': 'This is a new list',
        'this_is_true': True,
        'my_number': 1234,
        'my_longer_list': [987, 654, 'abc', 'xyz']
    }
    return render(request, 'home.html', my_context)


def ListView(request, *args, **kwargs):
    obj = Post.objects.get(id=1)
    context = {
        'object': obj
    }
    return render(request, 'post/post_detail_view.html', context)


def PostCreateView(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }
    return render(request, 'post/post_create.html', context)
