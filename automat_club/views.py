from django.shortcuts import render


def home_view(request):
    return render(request, 'home.html')


def about_us_view(request):
    return render(request, 'about_us.html')
