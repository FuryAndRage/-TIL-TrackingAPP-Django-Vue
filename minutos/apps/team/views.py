from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Team

@login_required
def add(request):
    if request.method == 'POST':
       title = request.POST.get('title')
       if title:
           team = Team.objects.create(title = title, created_by=request.user)
           team.members.add(request.user)
           team.save()

           userprofile = request.user
           userprofile.active_team_id = team.id
           userprofile.save()

           return redirect('userprofile:myaccount')
    return render(request, 'team_add.html') 