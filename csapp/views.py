from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django import forms

to_do = ['study german','programming','courses','talking']

class DutyForm(forms.Form):
    your_duty = forms.CharField(label='Your duty', max_length=100)


def index(request):
	return render(request, 'csapp/index.html',context = {
		"to_do":to_do
		})

def form_ask(request):
    if request.method == "POST":
        myform = DutyForm(request.POST)
        duty_name = request.POST.get('your_duty')
        if myform.is_valid():
            to_do.append(duty_name)
            
    else:
        myform = DutyForm()

    return render(request, 'csapp/formask.html',context = {"myform":myform})	