from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings


def home_view(request):
    return render(request, 'home.html')


def about_us_view(request):
    return render(request, 'about_us.html')


def contact_view(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form_email = form.cleaned_data.get('email')
        form_message = form.cleaned_data.get('tresc')
        form_full_name = form.cleaned_data.get('nazwa')
        subject = 'Kontakt, www KNA'
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email]
        contact_message = f"{form_full_name}:\n{form_message}\nwysłany przez {form_email}"
        send_mail(subject,
                  contact_message,
                  from_email,
                  to_email,
                  fail_silently=False)
    context = {
        "form": form,
    }
    return render(request, "contact.html", context)
