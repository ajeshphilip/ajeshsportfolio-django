from django.shortcuts import render
from website.models import MyApp


def index(request):
    all_apps = MyApp.objects.all()
    context = {
        'my_apps': all_apps,
        'page': request.path,
    }
    return render(request, 'website/index.html', context)

