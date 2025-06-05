from django.shortcuts import render , get_object_or_404
from .models import Article

# Create your views here.

def home(request):
    articles = Article.publish.all()
    return render(request,"blog/home.html",{"articles":articles})

def article_detail(request,slug):
    article = get_object_or_404(Article,slug=slug)
    
    return render(request,"blog/article.html",{"article":article})