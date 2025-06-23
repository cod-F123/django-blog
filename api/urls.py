from .views import blog_api_views , user_api_views
from django.urls import path 

urlpatterns = [
    path("all-blogs/",blog_api_views.get_all_article)
]
