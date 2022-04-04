from pathlib import Path
from app import views
from django.urls import path

urlpatterns = [
  path('', views.employees_api, name='main-index'),
]
