from django import template
from django.contrib.auth.models import User 
from accounts.models import Following

register = template.Library()

@register.filter(name="is_followed")
def is_followed(followed,follower):
    return Following.objects.filter(followd__username = followed,follower__username = follower).exists()