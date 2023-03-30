from django.shortcuts import render
# Create your views here.
# CRUD Create, Update

def home(request):
    name = 'home'
    return render(request, '../templates/home.html')