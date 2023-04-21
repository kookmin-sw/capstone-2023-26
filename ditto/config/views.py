from django.shortcuts import render

# Create your views here.

def home(request):
    name = 'home'
    return render(request, '../templates/home.html')

def main(request):
    name = 'main'
    return render(request, '../templates/main.html')

def test(request):
    name = 'test'
    return render(request, '../templates/administer.html')