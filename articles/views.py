from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Article


# Create your views here.

def article_list(request):
    articles = Article.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, "articlelist.html", {'articles': articles})



# views for homepage load-in
def article_post(request):
    articles = Article.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    last_article = articles[0]
    return render(request, "homepage.html", {'last_article': last_article})