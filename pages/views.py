from django.shortcuts import render
from django.http import HttpResponse

from realtors.models import Realtor, TeamSection

def index(request):
    realtors = Realtor.objects.all()
    teamsection = TeamSection.objects.all()
    context = {
        'realtors': realtors,
        'teamsection': teamsection
    }
    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')
