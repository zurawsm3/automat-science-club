from django.urls import path
from .views import recrutation_view, thanks_view

urlpatterns = [
    path('', recrutation_view),
    path('dzieki', thanks_view)
]