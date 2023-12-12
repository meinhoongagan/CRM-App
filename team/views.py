from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .forms import *
from .models import Team
# Create your views here.
def edit_team_views(request,pk):
    team=get_object_or_404(Team,created_by=request.user,pk=pk)
    if request.method=="POST":
        form=TeamForm(request.POST,instance=team)
        if form.is_valid():
            form.save()
            messages.success(request, "Team has been Changed")
            return redirect('myaccount')
    else:
        form = TeamForm(instance=team)
    return render(request,"team/edit_team.html",{
            "team":team,
            "form":form
    })