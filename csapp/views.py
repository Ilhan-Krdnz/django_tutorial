from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse
from django import forms
from .models import MyTasks

#This is global variable and it can be approached by everybody
#to_do = ['study german','programming','courses','talking']

class DutyForm(forms.Form):
    your_duty = forms.CharField(label='Add Duty', max_length=100)

class DeleteForm(forms.Form):
    duty_cancel = forms.CharField(label='Remove Duty', max_length=100)

def index(request):
    if 'to_do' not in request.session:
        #to_do is stored in request.session[],therefore its session variable. Also session is a dictionary
        request.session['to_do'] = []
    
    return render(request, 'csapp/index.html',context = {
		"to_do": request.session['to_do']
		})

def form_ask(request):
    if request.method == "POST":
        myform = DutyForm(request.POST)
        #clean_data wont work before running is_valid()!!
        if myform.is_valid():
            dbtask1 = MyTasks()
            request.session.modified = True
            dbtask1.task_name = myform.cleaned_data["your_duty"]
            request.session['to_do'].append(dbtask1) 
            return HttpResponseRedirect(reverse("csapp:index"))
    else:
        myform = DutyForm()

    return render(request, 'csapp/formask.html',context = {"myform":myform})

def form_delete(request):
    if request.method == 'POST':
        myform = DeleteForm(request.POST)
        if myform.is_valid():
            request.session.modified = True
            dutyname = myform.cleaned_data['duty_cancel']
            for i in request.session['to_do']:
                if i == dutyname:
                    request.session['to_do'].remove(dutyname)

            return HttpResponseRedirect(reverse("csapp:index"))
    else:
        myform = DeleteForm()
    return render(request, 'csapp/form_delete.html',context = {"myform":myform})	