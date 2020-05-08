from django.shortcuts import render


def logout(request):
    return render(request, 'registration/logged_out.html')


def logged(request):
    return render(request, 'registration/logged.html')
