from django.test import TestCase

# Create your tests here.

# a silly failing test
class SmokeTest(TestCase):
    def test_bad_maths(self):
        self.assertEqual(1 + 1, 3)