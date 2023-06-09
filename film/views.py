from django.shortcuts import render
from django.http import HttpResponse
from .models import Film
# Create your views here.

def home(request):
    wyszukiwanie = request.GET.get('szukajFilmu')
    if wyszukiwanie:
        moje_filmy = Film.objects.filter(title__icontains=wyszukiwanie)
    else:
        moje_filmy = Film.objects.all()
    return render(request, 'home.html', {'name': wyszukiwanie, 'filmy': moje_filmy})

def o_mnie(request):
    return render(request, 'about.html')

# def newsy(request):
#     return render(request, 'newsy.html')
