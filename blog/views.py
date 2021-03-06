from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post


# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, "bloglist.html", {'posts': posts})


def post_view(request, id):
    post = get_object_or_404(Post, pk=id)
    post.views += 1
    post.save()
    return render(request, "blogpost.html", {'post': post})


# views for homepage load-in
def last_post(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    last_post = posts[0]
    return render(request, "homepage.html", {'last_post': last_post})
