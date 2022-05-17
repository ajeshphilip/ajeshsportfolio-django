from django.shortcuts import render
from website.models import MyApp


def index(request):

    return render(request, 'website/index.html')


def samples(request):
    return render(request, 'website/samples.html')
