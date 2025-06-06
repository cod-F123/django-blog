from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login , logout
from .froms import RegisterUser
from django.contrib import messages
from .models import Profile
from django.contrib.auth.models import User

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