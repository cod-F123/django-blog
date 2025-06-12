from django import forms 
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm , UserChangeForm ,PasswordChangeForm
from .models import Profile

class RegisterUser(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ["username","email","password1","password2"]
        
    
class UpdateAccount(UserChangeForm):
    password = None
    
    username = forms.CharField(
        max_length=255,
        label="",
        widget= forms.TextInput(attrs={"class":"input-control","placeholder":"username"}),
        required= False
    )
    
    email = forms.EmailField(
        label="",
        max_length=255,
        widget= forms.EmailInput(attrs={"class":"input-control","placeholder":"email"}),
        required=False
    )
    
    first_name = forms.CharField(
        label="",
        max_length=255,
        widget= forms.TextInput(attrs={"class":"input-control","placeholder":"first name"}),
        required= False
    )
    
    last_name = forms.CharField(
        label="",
        max_length=255,
        widget= forms.TextInput(attrs={"class":"input-control","placeholder":"last name"}),
        required= False
    )
    
    class Meta:
        model = get_user_model()
        
        fields = ['first_name',"last_name","username","email"]
        

class ProfileForm(forms.ModelForm):
    image = forms.ImageField(
        label="",
        widget= forms.FileInput(attrs={"class":"input-control"}),
        required= False
    )
    
    description = forms.CharField(
        label="",
        widget= forms.Textarea(attrs={"class":"textarea-control","placeholder":"description"}),
        required= False
    )
    
    university = forms.CharField(
        label="",
        max_length=255,
        widget= forms.TextInput(attrs={"class":"input-control","placeholder":"university"}),
        required= False
    )
    
    class Meta:
        model = Profile
        
        fields = ["image","description","university"]
        
        
class UpdatePassword(PasswordChangeForm):
    old_password = forms.CharField(
        max_length=255,
        label="",
        widget= forms.PasswordInput(attrs={"class":"input-control","placeholder":"old password"}),
        required= True
    )
    
    new_password1 = forms.CharField(
        max_length=255,
        label="",
        widget= forms.PasswordInput(attrs={"class":"input-control","placeholder":"new password"}),
        required= True
    )
    
    new_password2 = forms.CharField(
        max_length=255,
        label="",
        widget= forms.PasswordInput(attrs={"class":"input-control","placeholder":"confirm new password"}),
        required= True
    )
    
    class Meta:
        model = get_user_model()
        fields = ["old_password","new_password1","new_password2",]