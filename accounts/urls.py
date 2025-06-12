from django.urls import path
from . import views


urlpatterns = [
    path("login/",views.login_user,name="login"),
    path("logout/",views.logout_user,name="logout"),
    path("register/",views.register_user,name="register"),
    path("user/<str:username>/",views.profile_page,name="profile_user"),
    path("following_user/",views.following_user,name="following_user"),
    path("unfollowing_user/",views.unfollowing_user,name="unfollowing_user"),
    path("account-info/", views.account_info, name="account_info"),
    path("user-info/", views.user_info, name="user_info"),
    path("change-password/",views.change_password, name="change_password"),
    path("delete-account/",views.delete_account, name= "delete_account"),
]
