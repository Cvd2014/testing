from django.shortcuts import render
from blog.models import Post
from django.utils import timezone
from articles.models import Article


# Create your views here.
def get_index(request):
    last_post = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[0]
    last_article = Article.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[0]
    return render(request, "homepage.html", {'last_post': last_post, 'last_article': last_article})
