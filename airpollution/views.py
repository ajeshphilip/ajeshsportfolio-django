from django.shortcuts import render

# Create your views here.


def welcome(request):
    print('hello')
    context = {
        'view_name': request.resolver_match.view_name,
    }
    return render(request, 'airpollution/welcome.html', context)
