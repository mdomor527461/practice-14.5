from django.shortcuts import render
from first_app.forms import PracticeForm
from . import models,forms
# Create your views here.

def form(request):
    form = PracticeForm()
    print(form)
    return render(request,'form.html',{'form' : form})


def employ_form(request):
    form = forms.EmployForm()
    print(form)
    return render(request,'model_form.html',{'form' : form})
