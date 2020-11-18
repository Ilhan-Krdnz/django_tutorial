from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse
from django import forms

#This is global variable and it can be approached by everybody
#to_do = ['study german','programming','courses','talking']

class DutyForm(forms.Form):
    your_duty = forms.CharField(label='Your duty', max_length=100)


def index(request):
    if 'to_do' not in request.session:
        #to_do is stored in request.session[],therefore its session variable. Also session is a dictionary
        request.session['to_do'] = ['hello','HI']
    
    return render(request, 'csapp/index.html',context = {
		"to_do": request.session['to_do']
		})

def form_ask(request):
    if request.method == "POST":
        myform = DutyForm(request.POST)
        #clean_data wont work before running is_valid()!!
        if myform.is_valid():
            duty_name = myform.cleaned_data["your_duty"]
            request.session['to_do'] += ['tudy_name'] 
            return HttpResponseRedirect(reverse("csapp:index"))
    else:
        myform = DutyForm()

    return render(request, 'csapp/formask.html',context = {"myform":myform})	