from django.shortcuts import render
from django.http import HttpResponse
from .models import plants as plants

def home(request):
    return HttpResponse('<h1>Test</h1>')

def about(request):
    return render(request, 'about.html')

def plants_index(request):
    return render(request, 'plants/index.html', {
        'plants': plants,
    })

# Create your views here.
