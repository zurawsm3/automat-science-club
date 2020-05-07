from django.shortcuts import render

# Create your views here.
from django_registration.views import RegistrationView

from django_registration.forms import RegistrationForm


class Myview(RegistrationView):
    # if RegistrationForm()
    def register(self, form):
        print("FFFFFFF")
        return super().register(form)
