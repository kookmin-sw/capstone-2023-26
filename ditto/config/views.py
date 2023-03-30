from django.shortcuts import render
from django.http import StreamingHttpResponse

# Create your views here.

def home(request):
    name = 'home'
    return render(request, '../templates/home.html')