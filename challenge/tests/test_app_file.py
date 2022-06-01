from django.apps import apps
from django.test import TestCase

from challenge.apps import ChallengeConfig


class CommentConfigTest(TestCase):
    """Test the challenge application in django on file apps.py"""

    def test_apps(self):
        self.assertEqual(ChallengeConfig.name, 'challenge')
        self.assertEqual(apps.get_app_config('challenge').name, 'challenge')
