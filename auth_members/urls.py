from django.urls import path, include
from .views import Myview

urlpatterns = [
    path('', include('django_registration.backends.activation.urls')),
    path('', include('django.contrib.auth.urls')),
    # path('register2/', Myview.as_view())
]
