from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

CHALLENGE_URL = reverse('challenge:challenge')

class PublicChallengeAPiTest(TestCase):
    """
    Test api access
    """

    def setUp(self):
        self.client = APIClient()

    def test_retrieve_challenge_if_number_is_not_found(self):
        """Test retrieving and challenge where the number param is not found"""
        res = self.client.get(CHALLENGE_URL)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(res.data, {'errors':'User Input is required.'})

    def test_retrieve_challenge_if_number_is_not_valid(self):
        """Test retrieving and challenge where the number param is not valid"""
        res = self.client.get('{}?number={}'.format(CHALLENGE_URL, "test"))

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(res.data, {'errors':'User Input must be an integer'})

    def test_retrieve_challenge_if_number_is_multiple_of_5(self):
        """Test retrieving and challenge where the number param is multiple of 5"""
        res = self.client.get('{}?number={}'.format(CHALLENGE_URL, 10))

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, 'L')

    def test_retrieve_challenge_if_number_is_multiple_of_7(self):
        """Test retrieving and challenge where the number param is multiple of 7"""
        res = self.client.get('{}?number={}'.format(CHALLENGE_URL, 14))

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, 'R')


    def test_retrieve_challenge_if_number_is_multiple_of_5_and_7(self):
        """Test retrieving and challenge where the number param is multiple of 5 & 7"""
        res = self.client.get('{}?number={}'.format(CHALLENGE_URL, 0))

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, 'LR')


    def test_retrieve_challenge_if_number_is_not_multiple_of_5_or_7(self):
        """Test retrieving and challenge where the number param is multiple of either 5 or 7"""
        res = self.client.get('{}?number={}'.format(CHALLENGE_URL, 6))

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, 6)
