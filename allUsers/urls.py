from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'homepage'),
    path('about/', views.about, name = 'about'),
    path('teacher/', views.teacher, name = 'teacher'),
    path('contact/', views.contact, name = 'contact'),
    path('login/', views.loginuser, name = 'login'),
    path('registration/', views.user_registration, name = 'registration'),
    path('logout/', views.logoutuser, name = 'logout'),
]
