from django.urls import path
from . import views

urlpatterns = [
    path('update_post/<int:pk>/', views.PianoUpdate.as_view()),
    path('create_post/', views.PianoCreate.as_view()),
    path('category/<str:slug>/', views.category_page),
    path('', views.PianoList.as_view()),  # shopping/
    path('<int:pk>/', views.PianoDetail.as_view()),  # shopping/1/
]