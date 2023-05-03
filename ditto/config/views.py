from django.shortcuts import render

# Create your views here.

def home(request):
    name = 'home'
    return render(request, '../templates/home.html')

def main(request):
    name = 'main'
    return render(request, '../templates/user/main.html')

def map(request):
    name = 'map'
    return render(request, '../templates/map.html')

def test(request):
    name = 'test'
    return render(request, '../templates/admin/administer.html')

def administer(request):
    name = 'admin'
    return render(request, '../templates/admin/main.html')

def detail(request):
    name = 'detail'
    return render(request, '../templates/admin/detail.html')