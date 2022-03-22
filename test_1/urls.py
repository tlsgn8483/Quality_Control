from django.urls import path
from . import views

from test_1.views import MainView

app_name = 'test_1'

urlpatterns = [
    path('main/', MainView.as_view(), name='main'),
]