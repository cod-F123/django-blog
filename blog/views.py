from django.shortcuts import render , get_object_or_404 , redirect
from django.urls import reverse
from django.forms import inlineformset_factory 
from .models import Article , Paragraph
from .forms import ArticleForm , ParagraphForm
from django.contrib import messages
from accounts.models import Profile

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

def update_blog(request,slug):
    if request.user.is_authenticated :
        article = Article.objects.filter(slug = slug).first()
        
        if article and article.author.username == request.user.username:
            article_form = ArticleForm(instance=article)
            FormSet = inlineformset_factory(Article,Paragraph,form=ParagraphForm, extra=0)
            
            form_set = FormSet(instance=article)
            
            if request.method == 'POST':
                article_form = ArticleForm(request.POST or None ,request.FILES or None, instance= article)
                form_set = FormSet(request.POST or None , request.FILES or None , instance=article)
                
                if article_form.is_valid() and form_set.is_valid():
                    article_form.save()
                    
                    form_set.save()
                    
                    messages.success(request,"Blog Updated")
                    return redirect(reverse("article_detail",args=[article.slug]))
                
                else:
                    for err in list(form_set.errors):
                        messages.error(request,err)
                    
                    for error in list(article_form.errors.values()):
                        messages.error(request,error)
                    
                    return redirect(reverse("update_blog",args=[article.slug]))
            
            return render(request,"blog/update-blog.html",{"form_set":form_set,"article_form":article_form})
        
        messages.success(request,"not founded")
        return redirect("home")
    
    messages.success(request,"Access Diend")
    return redirect("home")


def blogs_page(request):
    articles = Article.publish.all().order_by("date_created")
    newest_article = Article.publish.all().order_by("-date_created")
    author_p = Profile.objects.all().order_by("-followers")
    return render(request,"blog/blogs.html",{"articles":articles,"newest":newest_article,"author_p":author_p})
            
            