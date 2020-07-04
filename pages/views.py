from django.shortcuts import render
from django.http import HttpResponse

from realtors.models import Realtor

def index(request):
    realtors = Realtor.objects.all()
    context = {
        'realtors': realtors
    }
    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')
