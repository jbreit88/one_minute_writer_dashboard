from django.test import TestCase
from django.urls import reverse 
from rest_framework.test import APIClient 
from rest_framework import status 

from dashboard.models import WritingInfo
from dashboard.serializers import DashboardMetricsSerializer

CREATE_DASHBOARD_URL = reverse('dashboard:dashboard_list')

class PublicDashboardAPITests(TestCase):

  def setUp(self): 
    self.client = APIClient()

  def test_get_dashboard_metrics_success(self):
    """Test retreiving dashboard metrics with valid payload is successful"""
    WritingInfo.objects.create(id = 1, writing_id = 1, word_count = 100, time_spent = 200,)
     
    payload = {
      'writing_ids': '1',
    }

    response = self.client.get(CREATE_DASHBOARD_URL, payload)

    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_get_dashboard_metrics_fail(self):
    """Test that a payload with a writing id that doesn't exist fails"""
    WritingInfo.objects.create(id = 1, writing_id = 1, word_count = 100, time_spent = 200,)

    payload = {
      'writing_ids': '2'
    }

    response = self.client.get(CREATE_DASHBOARD_URL, payload)
    
    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
  
  def test_get_dashboard_metrics_success_multiple(self):
    """Test that a payload can have multiple ids and return a 200"""
    WritingInfo.objects.create(id = 1, writing_id = 1, word_count = 100, time_spent = 200,)
    WritingInfo.objects.create(id = 2, writing_id = 2, word_count = 50, time_spent = 150,)
    id_list = ['1', '2']
    
    payload = {
      'writing_ids': ','.join(id_list)
    }

    response = self.client.get(CREATE_DASHBOARD_URL, payload)

    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_get_dashboard_metrics_fail_multiple(self):
    """Test that a respons will fail with multiple incorrect payload variables"""
    WritingInfo.objects.create(id = 1, writing_id = 1, word_count = 100, time_spent = 200,)
    id_list = ['2', '3', '4']

    payload = {
      'writing_ids': ','.join(id_list)
    }

    response = self.client.get(CREATE_DASHBOARD_URL, payload)

    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

  def test_get_dashboard_metrics_fail_mixture(self):
    """Test that a response will fail with mix of correct and incorrect payload variables"""
    WritingInfo.objects.create(id = 1, writing_id = 5, word_count = 100, time_spent = 200,)
    id_list = ['2', '3', '5', '4']

    payload = {
      'writing_ids': ','.join(id_list)
    }

    response = self.client.get(CREATE_DASHBOARD_URL, payload)

    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    #Post Tests 
    #http://127.0.0.1:8000/dashboard?writing_id=21&total_time=100&word_count=50

    #Happy Paths 
    
  def test_post_dashboard_metrics_success(self): 
    """Test Post dashboard metrics with proper payload is successful"""

    payload = {
      'writing_id': 1,
      'total_time': 100, 
      'word_count': 50
    }

    response = self.client.post(CREATE_DASHBOARD_URL, payload)

    self.assertEqual(response.status_code, status.HTTP_201_CREATED)