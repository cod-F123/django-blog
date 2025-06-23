from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login , logout
from .froms import RegisterUser , UpdateAccount , ProfileForm , UpdatePassword
from django.contrib import messages
from .models import Profile , Following
from django.contrib.auth.models import User
from django.http import JsonResponse

# Create your views here.

def login_user(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request,"Login successful")
                return redirect("home")
            
            messages.error(request,"Login failed")
        return render(request,"accounts/login.html",{})

    return redirect("home")

def logout_user(request):
    logout(request)
    
    messages.success(request,"Logout successful")
    return redirect("home")

def register_user(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = RegisterUser(request.POST)
            
            if form.is_valid():
                form.save()
                user = authenticate(request,username=form.cleaned_data.get("username"), password=form.cleaned_data.get("password2"))
                login(request, user)
                messages.success(request, "Registration successful")

                return redirect("home")
            else:
                for error in form.errors:
                    messages.error(request, form.errors[error])
                return redirect("login")

    messages.error(request,"Access Denied")
    return redirect("home")


def profile_page(request,username):
    user = User.objects.filter(username = username).first()
    
    if user is not None:
        
        return render(request,"accounts/account.html",{"user_":user})
    
    messages.warning(request,"User not founded!")
    return redirect("home")

def following_user(request):
    if request.user.is_authenticated:
        if request.method == 'POST' and request.POST.get("action") == 'post':
            followed_user = User.objects.filter(username = request.POST.get("uname")).first()
            
            if followed_user is not None:
                followed_last = Following.objects.filter(followd__username = followed_user.username , follower__username = request.user.username).first() 

                if followed_last is None:
                    new_followed = Following.objects.create(followd = followed_user,follower = request.user)
                    
                    followed_user.profile.followers = followed_user.follower.all().count()
                    
                    followed_user.profile.save()
                    
                    return JsonResponse({"message":"successful"})
                
    return JsonResponse({"message":"error"})

def unfollowing_user(request):
    if request.user.is_authenticated:
        if request.method == 'POST' and request.POST.get("action") == 'post':
            followed_user = User.objects.filter(username = request.POST.get("uname")).first()
            
            if followed_user is not None:
                followed_last = Following.objects.filter(followd__username = followed_user.username , follower__username = request.user.username).first() 

                if followed_last is not None:
                    followed_last.delete()
                    
                    followed_user.profile.followers = followed_user.follower.all().count()
                    
                    followed_user.profile.save()
                    
                    return JsonResponse({"message":"successful"})
                
    return JsonResponse({"message":"error"})

def account_info(request):
    if request.user.is_authenticated:
        user_form = UpdateAccount(instance = request.user)
        
        if request.method == 'POST':
            user_form = UpdateAccount(request.POST or None , instance = request.user)
            
            if user_form.is_valid():
                user_form.save()
                
                messages.success(request,"Account Updated!")
                
                return redirect("account_info")
            
            else:
                for err in list(user_form.errors.values()):
                    messages.error(request,err)
                
                return redirect("account_info")
            
        return render(request, "accounts/account-info.html",{"user_form":user_form})
    
    messages.error(request,"Access Denied")
    return redirect("login")            

def user_info(request):
    if request.user.is_authenticated:
        user_form = ProfileForm(instance = request.user.profile)
        
        if request.method == 'POST':
            user_form = ProfileForm(request.POST or None, request.FILES or None, instance = request.user.profile)
            
            if user_form.is_valid():
                user_form.save()
                
                messages.success(request,"User info Updated!")
                
                return redirect("user_info")
            
            else:
                for err in list(user_form.errors.values()):
                    messages.error(request,err)
                
                return redirect("user_info")
            
        return render(request, "accounts/user-info.html",{"user_form":user_form})
    
    messages.error(request,"Access Denied")
    return redirect("login")         

def change_password(request):
    if request.user.is_authenticated:
        form = UpdatePassword(request.user)
        
        if request.method == 'POST':
            form = UpdatePassword(request.user, request.POST or None)
            
            if form.is_valid():
                form.save()
                
                login(request,request.user)   
                
                messages.success(request,"password changed")
                
                return redirect("home")
            
            else:
                for err in list(form.errors.values()):
                    messages.error(request,err)
                
                return redirect("change_password")
        
        return render(request,"accounts/change-password.html",{"form":form})
    
    messages.error(request,"Access Denied")
    return redirect("login")

def delete_account(request):
    if request.user.is_authenticated:
        user = User.objects.filter(username = request.user.username).first()
        
        logout(request)
        
        user.delete()
        
        messages.success(request,"Yout account deleted")
        return redirect("home")
    
    messages.error(request,"Access Denied")
    return redirect("login") 