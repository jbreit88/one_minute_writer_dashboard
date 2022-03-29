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
