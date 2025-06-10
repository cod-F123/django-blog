from django.shortcuts import render , get_object_or_404 , redirect
from django.forms import inlineformset_factory
from .models import Article , Paragraph
from .forms import ArticleForm , ParagraphForm
from django.contrib import messages

# Create your views here.

def home(request):
    articles = Article.publish.all()
    return render(request,"blog/home.html",{"articles":articles})

def article_detail(request,slug):
    article = get_object_or_404(Article,slug=slug)
    
    return render(request,"blog/article.html",{"article":article})

def new_blog(request):
    if request.user.is_authenticated:
        article_form = ArticleForm()
        FormSet = inlineformset_factory(Article,Paragraph,form=ParagraphForm,extra=1,can_delete=False)
        
        form_set = FormSet()
        if request.method == 'POST':
            article_form = ArticleForm(request.POST or None, request.FILES or None)
            form_set = FormSet(request.POST or None , request.FILES or None)
            print(1)
            
            if article_form.is_valid() and form_set.is_valid():
                print(2)
                article_form.instance.author = request.user
                art_form = article_form.save()
                
                para_forms = form_set.save(commit=False)
                
                for form in para_forms:
                    form.article = art_form
                    form.save()
                
                return redirect("home")
            
            else:
                messages.success(request,"Invalid data")
                print(form_set.errors)
                print(article_form.errors)
                return redirect("new_blog")
                
        return render(request,"blog/newBlog.html",{"article_form":article_form,"form_set":form_set})

    return redirect("login")