from dataclasses import field
import email
import imp
from django import forms
from django.contrib.auth.models import User
from .models import userProfile, contactPage
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

        labels = {
            'password1' : 'Password',
            'password2' : 'Confirm password'
        }

class UserProfileForm(forms.ModelForm):
    bio = forms.CharField(required=False)

    teacher = 'teacher'
    student = 'student'
    parent = 'parent'

    user_type = [(student, 'student'), (parent, 'parent')]

    user_choice = forms.ChoiceField(required=True, choices=user_type)

    class Meta:
        model = userProfile
        fields = ('bio', 'profile_pic', 'user_choice')

class contactForm(forms.ModelForm):
    class Meta:
        model = contactPage
        fields = "__all__"
        
    