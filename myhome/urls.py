from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('my_page/', views.my_page),
    path('about_company/', views.about_company),
]