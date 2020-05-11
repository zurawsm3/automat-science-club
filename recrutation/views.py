from django.shortcuts import render
from .forms import RecruitmentForm
from .models import Recruiter


def recrutation_view(request):
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
    # title = "Rekrutacja"
    # form = SignUpForm(request.POST or None)
    #
    # context = {
    #     "title": title,
    #     "form": form,
    # }
    # if form.is_valid():
    #     form.save()
    #     context = {
    #         "title": "Dziekujemy"
    #     }
    # if request.user.is_authenticated() :

    context = {
        "queryset": Recruiter.objects.filter(status='a')
    }
    return render(request, 'members.html', context)
