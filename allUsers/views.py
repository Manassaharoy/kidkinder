from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import contactPage, userProfile
from allUsers.forms import UserForm, UserProfileForm, contactForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    teachers = userProfile.objects.filter(user_choice='teacher')
    parents = userProfile.objects.filter(user_choice='parent')
    return render(request, 'index.html', {'teachers':teachers, 'parents':parents})

def about(request):
    teachers = userProfile.objects.filter(user_choice='teacher')

    return render(request, 'about.html',{'teachers':teachers})

def teacher(request):
    teachers = userProfile.objects.filter(user_choice='teacher')
    return render(request, 'teachers.html', {'teachers':teachers})

#one_way
# def contact(request):
#     if request.method == "POST":
#         form = contactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             form = contactForm()
#             return render(request, 'contact.html', {'form':form})
#     form = contactForm()
#     return render(request, 'contact.html', {'form':form})

#another_way
def contact(request):
    if request.method == "POST":
        contact = contactPage()
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact.name = name
        contact.email = email
        contact.subject = subject
        contact.message = message
        contact.save()
        
    return render(request, 'contact.html')


def user_registration(request):
    registered = False

    if request.method == 'POST':
        userform = UserForm(data=request.POST)
        userprofileform = UserProfileForm(data=request.POST)
        if userform.is_valid() and userprofileform.is_valid():
            user = userform.save()
            user.save()

            profile = userprofileform.save(commit = False)
            profile.user = user
            profile.save()

            registered = True
        else:
            print(userform.errors, userprofileform.errors)
    else:
        userform = UserForm()
        userprofileform = UserProfileForm()
    return render(request, 'register.html', {'userform' : userform, 'userprofileform' :  userprofileform, 'registered' : registered})

def loginuser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('homepage'))
            else:
                return HttpResponse("Account is not active, contact admin")
        else:
            return HttpResponse("Account is not active, contact admin")
    else:
        return render(request, 'login.html')

@login_required
def logoutuser(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))