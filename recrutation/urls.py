from django.urls import path
from .views import recrutation_view, thanks_view, members_view

urlpatterns = [
    path('', recrutation_view),
    path('dzieki', thanks_view),
    path('czlonkowie/', members_view),
]