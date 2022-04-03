from django.test import TestCase
from dashboard.models import StringManipulation
from unittest import skip

class StringManipulationModelTest(TestCase):
  def test_char_split_method(self):
    """Test the char split method for expected resutls"""

    string = "Python"

    self.assertEqual(StringManipulation.char_split(string), ['P', 'y', 't', 'h', 'o', 'n'])