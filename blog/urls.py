from django.urls import path 
from . import views 

urlpatterns = [
    path("",views.home,name="home"),
    path("blog/<str:slug>/",views.article_detail,name="article_detail"),
    path("new/",views.new_blog,name="new_blog"),
    path("update/blog/<str:slug>/",views.update_blog , name="update_blog"),
    path("blogs/",views.blogs_page, name="blogs"),
    path("update-comment/<int:pk>/",views.update_comment,name="update_comment"),
    path("deletecomment-deletecomment-delete/",views.delete_comment , name="delete_comment"),
]
