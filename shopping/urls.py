from django.urls import path
from . import views

urlpatterns = [
    path('', views.PianoList.as_view()),  # shopping/
    path('<int:pk>/', views.PianoDetail.as_view()),  # shopping/1/
]