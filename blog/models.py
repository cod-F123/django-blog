from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
import random

User = get_user_model()

# Create your models here.


class ArticlePublishedManager(models.Manager):
    def get_queryset(self):
        return super(ArticlePublishedManager,self).get_queryset().filter(status = "published")

class Article(models.Model):
    ARTICLE_STATUS = (
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('rejected', 'Rejected'),
    )
    
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="upload/articles/images")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    mini_description = models.TextField(max_length=255)
    
    introduction = models.TextField(blank=True,null=True)
    
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    status = models.CharField(max_length=200,choices=ARTICLE_STATUS, default='draft')
    
    tags = models.CharField(max_length=255,blank=True,null=True)
    
    slug  = models.SlugField(blank=True,null=True,max_length=255)
    
    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
        
        ordering = ("-date_created",)
        
    def save(self,*args,**kwargs):
        if not self.slug:
            random_num = random.randint(10000,99999)
            self.slug = str(self.title)+str(self.author)+str(random_num)
            self.save()
        
        super().save(*args,**kwargs)
    
    objects = models.Manager()
    publish = ArticlePublishedManager()
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"slug": self.slug})
    
    

class Paragraph(models.Model):
    STATUS = (
        ('rejected', 'Rejected'),
        ('published', 'Published'),
    )
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    title = models.CharField(max_length=255,blank=True , null=True)
    content = models.TextField()
    image = models.ImageField(upload_to="upload/articles/paragraphs/images", blank=True, null=True)
    status = models.CharField(max_length=200, choices=STATUS, default='published')
    
    
    class Meta:
        verbose_name = "Paragraph"
        verbose_name_plural = "Paragraphs"
        
    def __str__(self):
        return f"Paragraph {self.id} of {self.article.title}"
    
    

class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    content = models.CharField(max_length=255)
    
    date_created = models.DateField(auto_now_add=True)
    
    date_updated = models.DateField(auto_now=True)
    
    updated = models.BooleanField(default=False)
    
    def __str__(self):
        return self.article.title
    