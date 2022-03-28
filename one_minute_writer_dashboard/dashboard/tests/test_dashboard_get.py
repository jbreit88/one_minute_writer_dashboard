from django.test import TestCase
from django.urls import reverse 
from rest_framework.test import APIClient 
from rest_framework import status 

from dashboard.models import WritingInfo
from dashboard.serializers import DashboardMetricsSerializer

CREATE_DASHBOARD_URL = reverse('dashboard:dashboard_list')
# import ipdb; ipdb. set_trace() 

def test_get_dashboard_metrics_success(self):
  """Test retreiving dashboard metrics with valid payload is successful"""
  payload = {
    
  }
