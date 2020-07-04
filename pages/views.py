from django.shortcuts import render
from django.http import HttpResponse

from realtors.models import Realtor, TeamSection
from listings.models import Portfolio, PortfolioSection, ServicesSection, Services

def index(request):
    realtors = Realtor.objects.all()
    teamsection = TeamSection.objects.all()

    portfolio = Portfolio.objects.all()
    portfoliosection = PortfolioSection.objects.all()

    services = Services.objects.all()
    servicessection = ServicesSection.objects.all()

    context = {
        'realtors': realtors,
        'teamsection': teamsection,

        'portfolio': portfolio,
        'portfoliosection': portfoliosection,

        'services': services,
        'servicessection': servicessection       
    }
    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')
