from django.conf.urls import url
from dashboard import views

app_name = 'dashboard'

urlpatterns = [
    url('dashboard', views.dashboard_list, name='dashboard_list'),
    # url(r'^api/tutorials/(?P<pk>[0-9]+)$', views.tutorial_detail),
    # url(r'^api/tutorials/published$', views.tutorial_list_published)
]
