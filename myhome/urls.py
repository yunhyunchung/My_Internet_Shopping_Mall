from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing),
    path('my_page/', views.my_page),
    path('about_company/', views.about_company),
]