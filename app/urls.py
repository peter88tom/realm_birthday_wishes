from pathlib import Path
from app import views
from django.urls import path

urlpatterns = [
  path('', views.home_page, name='main-index'),
]
