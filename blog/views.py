from django.shortcuts import render
from django.http import HttpResponse
from .models import ArticlePost
# Create your views here.

def blog_base(request):
    return render(request, 'blog/base.html')

def article_list(request):
    articles = ArticlePost.objects.all()
    context = {'articles': articles}
    return render(request, 'blog/list.html', context)


