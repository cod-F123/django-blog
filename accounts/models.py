from django.db import models
from django.db.models.signals import post_save 
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="upload/user/images",default="default/images/user.png")
    
    description = models.TextField(blank=True,null=True)
    
    university = models.CharField(max_length=255,blank=True,null=True)
    
    def __str__(self):
        return self.user.username 
    
def create_profile(sender, instance, created,**kwargs):
    if created:
        user_profile = Profile(user = instance)
        user_profile.save()

post_save.connect(create_profile,sender = User)


class Following(models.Model):
    followd = models.ForeignKey(User,on_delete= models.CASCADE, related_name="follower")
    follower = models.ForeignKey(User,on_delete= models.CASCADE, related_name="followed")
    
    date_followed = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.follower.username} -> {self.followd.username}"