from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from .forms import UserForm
@login_required(login_url='user/login')
def index(request):

    return render(request, 'user/index.html')

def login(request):
    form = UserForm(request.POST)
    if request.method == 'POST':

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username,password=password)
        if user != None:
            auth_login(request, user)
            return HttpResponseRedirect(reverse("user:index"))
        else:
            return render(request, 'user/login.html',context={
        "error":"invalid password or username"
        })
    return render(request, 'user/login.html',context={
        "form":form
        })

def logout(request):
    return render(request, 'user/logout.html')