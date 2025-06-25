from .views import blog_api_views , user_api_views
from rest_framework_simplejwt.views import TokenObtainPairView , TokenRefreshView , TokenVerifyView
from django.urls import path 

urlpatterns = [
    path("all-blogs/",blog_api_views.ListCreateBlog.as_view()),
    path("login/",TokenObtainPairView.as_view(),name="login-api"),
    path("represh-token/",TokenRefreshView.as_view(),name="refresh-token"),
    path("verify-token/",TokenVerifyView.as_view(),name="token-verify"),
]
