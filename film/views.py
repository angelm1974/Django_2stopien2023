from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html', {'name':'Janusz'})

def o_mnie(request):
    return HttpResponse("<H1 style='color:red;'>To jest moja strona</H1>")