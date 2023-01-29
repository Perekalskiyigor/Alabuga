from django.shortcuts import render
from .models import Citizen, Workers

def index(request):
    template = 'model/index.html'
    citizen = Citizen.objects.order_by('name')
    context = {
        'citizen': citizen,
    }
    return render(request, template, context) 

