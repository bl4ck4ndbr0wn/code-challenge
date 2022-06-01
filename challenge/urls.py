from django.urls import path

from .views import (RetrieveMultiplesAPIView,)

urlpatterns = [
    path('LR', RetrieveMultiplesAPIView.as_view()),
]
