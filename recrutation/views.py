from django.shortcuts import render
from .forms import RecruitmentForm
from .models import Recruiter


def recruitment_view(request):
    form = RecruitmentForm(request.POST or None)
    context = {
        "title": "Formularz zgłoszeniowy",
        "form": form,
        "button": True,
    }
    if form.is_valid():
        form.save()
        context = {
            "title": "Rozpatrzymy Twoją prośbę"
        }
    return render(request, "recruitment.html", context)


def thanks_view(request):
    return render(request, "thanks.html")


def members_view(request):
    context = {
        "queryset": Recruiter.objects.filter(status='a')
    }
    return render(request, 'members.html', context)
