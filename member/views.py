from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect,render
from .models import *
def sign_up(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            member=member.objects.create(user=user)
        return redirect('/login/')
    else:
        form=UserCreationForm()
        return render(request,'authentication/signup.html',{'form':form})
def login_view(request):
    form=UserCreationForm()
    return render(request,'authentication/login.html',{'form':form})