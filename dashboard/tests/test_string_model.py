from django.test import TestCase
from django.urls import reverse 
from rest_framework.test import APIClient 
from rest_framework import status 

from dashboard.models import StringManipulation
from dashboard.serializers import DashboardMetricsSerializer

from unittest import skip

class StringManipulationModelTest(TestCase):
  def test_char_split_method(self):
    """Test the char split method for expected resutls"""

    string = "Python"

    self.assertEqual(StringManipulation.char_split(string), ['P', 'y', 't', 'h', 'o', 'n'])