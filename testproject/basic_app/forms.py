from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileModels

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileModels
        fields = ('user_portfolio_url', 'user_profile_pic')