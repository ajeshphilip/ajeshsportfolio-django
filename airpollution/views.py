from django.shortcuts import render

# Create your views here.


def welcome(request):
    print('hello')
    context = {
        'page': request.path,
    }
    return render(request, 'airpollution/welcome.html', context)
