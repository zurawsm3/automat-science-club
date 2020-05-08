from django.urls import path, include
from .views import logout, logged

urlpatterns = [
    path('', include('django_registration.backends.activation.urls')),
    path('', include('django.contrib.auth.urls')),
    path('logout', logout),
    path('zalogowano', logged),
]
