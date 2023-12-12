from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect,render
from .models import *
from team.models import Team
def sign_up(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            member=member.objects.create(user=user)
            team=Team.objects.create(name="The team name",created_by=request.user)
            team.member.add(request.user)
            team.save()
        return redirect('/login/')
    else:
        form=UserCreationForm()
        return render(request,'authentication/signup.html',{'form':form})
def login_view(request):
    form=UserCreationForm()
    return render(request,'authentication/login.html',{'form':form})
@login_required()
def my_account_view(request):
    team=Team.objects.filter(created_by=request.user)[0]
    return render(request,'authentication/member.html',{
        "team":team
    })