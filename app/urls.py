# app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page URL
     path('report/', views.report, name='report'),
     path('about/', views.about, name='about'),
]
