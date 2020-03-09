from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile,Post
from django.db import models


class UserRegistration(UserCreationForm):
    email=forms.EmailField(required=True)
    class Meta:
        model=User
        fields=('username','email','password1','password2')
    def save(self,commit=True):
        user=super().save(commit=False)
        user.email=self.cleaned_data['email']
        user.username=self.cleaned_data['username']
        if commit:
            user.save()
        return user

class UserProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=('rank',)

class LoginForm(forms.Form):
    username=forms.CharField(max_length=20,label="Enter Your Username")
    password=forms.CharField(widget=forms.PasswordInput)


class CreatePost(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','content',)

    def save(self ,commit=True):
        
        user=super().save(commit=False)
        user.title=self.cleaned_data['title']
        user.content=self.cleaned_data['content']
        if commit:
            user.save()
        return user
# class CreatePost(forms.ModelForm):
#     class Meta:
#         model=Post
#         fields=('title','content')
