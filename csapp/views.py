from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.core import serializers
from django.http import HttpResponse
from django import forms
from .models import MyTasks

#This is global variable and it can be approached by everybody
#to_do = ['study german','programming','courses','talking']

class DutyForm(forms.Form):
    your_duty = forms.CharField(label='Add Duty', max_length=100)

class DeleteForm(forms.Form):
    duty_cancel = forms.CharField(label='Remove Duty', max_length=100)

@login_required
def index(request):
    if 'to_do' not in request.session:
        #to_do is stored in request.session[],therefore its session variable. Also session is a dictionary
        request.session['to_do'] = []
    tasks = MyTasks.objects.filter(user=request.user)
    return render(request, 'csapp/index.html',context = {
		"to_do": tasks
		})

def form_ask(request):
    if request.method == "POST":
        myform = DutyForm(request.POST)
        #clean_data wont work before running is_valid()!!
        if myform.is_valid():
            #request.session.modified = True
            taskname = myform.cleaned_data["your_duty"]
            dbtask = MyTasks(task_name=str(taskname),user=request.user)
            dbtask.save()
            #serialized_obj = serializers.serialize('json', [ dbtask, ])
            #serialized_obj.save()
            #request.session['to_do'].append(dbtask)
            return HttpResponseRedirect(reverse("csapp:index"))
    else:
        myform = DutyForm()

    return render(request, 'csapp/formask.html',context = {"myform":myform})

def form_delete(request):
    if request.method == 'POST':
        myform = DeleteForm(request.POST)
        if myform.is_valid():
            #request.session.modified = True
            task = MyTasks.objects.all()
            dutyname = myform.cleaned_data['duty_cancel']
            for i in task:
                if str(i.task_name) == str(dutyname):
                    task.filter(task_name=i).delete()


            return HttpResponseRedirect(reverse("csapp:index"))
    else:
        myform = DeleteForm()
    return render(request, 'csapp/form_delete.html',context = {
        "myform":myform,
        })	