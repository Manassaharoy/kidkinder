from distutils.command import upload
from email.policy import default
from secrets import choice
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class userProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=150, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pictures', blank = True, default="cartoon-boy-images-11.jpg")

    teacher = 'teacher'
    student = 'student'
    parent = 'parent'

    user_type = [ (teacher, 'teacher'), (student, 'student'), (parent, 'parent')]

    user_choice = models.CharField(max_length=10, choices=user_type, default=student)
    
    def __str__(self):
        return f'{self.user.username} registered as {self.user_choice}'
    
class contactPage(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return f'{self.name}, subject: {self.subject}'