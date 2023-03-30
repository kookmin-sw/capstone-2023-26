from django.shortcuts import render

# Create your views here.

def home(request):
    name = 'home'
    return render(request, '../templates/home.html')