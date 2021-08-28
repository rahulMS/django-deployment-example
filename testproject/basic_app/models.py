from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileModels(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)

    user_portfolio_url = models.CharField(max_length=256, blank= True)
    user_profile_pic = models.ImageField(upload_to='profile_pics', blank=True)