from django.urls import path
from .views import recruitment_view, thanks_view, members_view

urlpatterns = [
    path('', recruitment_view),
    path('dzieki', thanks_view),
    path('czlonkowie/', members_view),
]