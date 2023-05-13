from django.shortcuts import render
# Create your views here.

def home(request):
    name = 'home'
    return render(request, '../templates/test.html')

def map(request):
    name = 'map'
    return render(request, '../templates/map.html')