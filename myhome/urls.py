from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),  # myhome/
    path('my_page/', views.my_page),  # myhome/about_me
]