from django.shortcuts import render
from .models import *


def index(request):
    context = dict()
    return render(request, 'komp/index.html', context)

def site(request):
    context = dict()
    return render(request, 'komp/site.html', context)


# Create your views here.
