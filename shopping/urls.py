from django.urls import path
from . import views

urlpatterns = [
    path('category/<str:slug>/', views.category_page),
    path('', views.PianoList.as_view()),  # shopping/
    path('<int:pk>/', views.PianoDetail.as_view()),  # shopping/1/
]