# app/urls.py
from django.urls import path
from . import views
from .views import signup_view, login_view, logout_view

urlpatterns = [
    path('', views.home, name='home'),  # Home page URL
    path('report/', views.report, name='report'),
    path('about/', views.about, name='about'),
    #  path('login/', views.login, name='login'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout' )
]
