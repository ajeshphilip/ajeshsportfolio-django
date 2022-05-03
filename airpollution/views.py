from django.shortcuts import render

# Create your views here.


def welcome(request):
    context = {
        'app_name': request.resolver_match.app_name,
    }
    return render(request, 'airpollution/welcome.html', context)


def upload_file(request):
    context = {
        'app_name': request.resolver_match.app_name,
        'message_success': 'File successfully uploaded',
    }
    return render(request, 'airpollution/welcome.html', context)

