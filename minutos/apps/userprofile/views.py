from django.contrib import auth, messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from minutos.apps.team.models import Team

from .models import UserProfile



def signup(request):
    form = UserCreationForm()
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.email = user.username
            user.save()

            userprofile = UserProfile.objects.create(user = user)
            login(request, user)
            return redirect('core:frontpage')
    return render(request, 'signup.html', {'form':form})

@login_required
def my_account(request):
    # teams = request.user.teams.all()
    print(request.user.userprofile)
    teams = request.user.teams.exclude(pk=request.user.id)
    
    return render(request, 'myaccount.html',{'teams':teams})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        request.user.first_name = request.POST.get('first_name', '')
        request.user.last_name = request.POST.get('last_name', '')
        request.user.email = request.POST.get('email', '')
        request.user.save()
        
        messages.info(request,'The changes was saved' )
        return redirect('userprofile:myaccount')
    return render(request, 'edit_profile.html')

def login(request):
    if request.user.is_authenticated:
        return redirect('userprofile:myaccount')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(request, username=username, password=password)

        if not user:
            messages.error(request, 'Username or password incorrect')
            return render(request, 'login.html')
        else:
            auth.login(request, user)
            return redirect('userprofile:myaccount')
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('core:frontpage')