from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

def challenge_url(number):
    return reverse("challenge:LR", args=[number])

class PublicChallengeAPiTest(TestCase):
    """
    Test api access
    """

    def setUp(self):
        self.client = APIClient()
