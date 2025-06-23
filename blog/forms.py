from django import forms
from .models import Article, Paragraph , Comment

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label="",
        max_length=255,
        widget= forms.TextInput(attrs={"class":"input-control","placeholder":"Title"}),
        required=True
    )
    image = forms.ImageField(
        label="",
        widget= forms.FileInput(attrs={"class":"input-control","placeholder":"image"}),
        required=True
    )
    mini_description = forms.CharField(
        label="",
        max_length=255,
        widget= forms.TextInput(attrs={"class":"input-control","placeholder":"Mini description"}),
        required=True
    )
    
    introduction = forms.CharField(
        label="",
        required=True,
        widget= forms.Textarea(attrs={"class":"textarea-control","placeholder":"Introduction"})
    )
    
    tags = forms.CharField(
        label="",
        max_length=255,
        widget= forms.TextInput(attrs={"class":"input-control","placeholder":"Tags(Optional)"}),
        required=False
    )
    
    class Meta:
        model = Article
        fields = ["title","image","mini_description","introduction","tags"]


class ParagraphForm(forms.ModelForm):
    title = forms.CharField(
        label="",
        max_length=255,
        widget= forms.TextInput(attrs={"class":"input-control","placeholder":"Title(Optional)"}),
        required=False
    )
    
    content = forms.CharField(
        label="",
        required=True,
        widget= forms.Textarea(attrs={"class":"textarea-control","placeholder":"Content"})
    )
    
    image = forms.ImageField(
        label="",
        widget= forms.FileInput(attrs={"class":"input-control","placeholder":"image"}),
        required=False
    )
    
    class Meta:
        model = Paragraph
        fields = ["title","content","image"]
        

class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label="",
        widget= forms.Textarea(attrs={"class":"textarea-control","placeholder":"content of comment"}),
        required=True
    )
    
    class Meta:
        model = Comment
        fields = ["content",]