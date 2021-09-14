from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    projects = Project.objects.all()
    experiences = Experience.objects.all()

    context = {'projects':projects,'experiences':experiences}
    return render(request, 'index.html', context)
