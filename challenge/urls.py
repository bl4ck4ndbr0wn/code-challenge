from django.urls import path

from .views import (RetrieveMultiplesAPIView,)

app_name = 'challenge'

urlpatterns = [
    path('challenge/', RetrieveMultiplesAPIView.as_view(), name="challenge"),
]
