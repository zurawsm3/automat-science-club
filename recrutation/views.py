from django.shortcuts import render
from .forms import RecruitmentForm


def recrutation_view(request):
    form = RecruitmentForm(request.POST or None)
    context = {
        "form": form,
    }
    if form.is_valid():
        form.save()
        context = {
            "title": "Dziekujemy"
        }
    return render(request, "recruitment.html", context)


def thanks_view(request):
    return render(request, "thanks.html")
