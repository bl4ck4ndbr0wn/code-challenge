from django.urls import path

from .views import (RetrieveMultiplesAPIView,)

urlpatterns = [
    path('', RetrieveMultiplesAPIView.as_view()),
]
