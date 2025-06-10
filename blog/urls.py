from django.urls import path 
from . import views 

urlpatterns = [
    path("",views.home,name="home"),
    path("blog/<str:slug>/",views.article_detail,name="article_detail"),
    path("new/",views.new_blog,name="new_blog"),
]
