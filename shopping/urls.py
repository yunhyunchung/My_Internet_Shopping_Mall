from django.urls import path
from . import views

urlpatterns = [
    path('search/<str:q>/', views.PianoSearch.as_view()),
    path('update_post/<int:pk>/', views.PianoUpdate.as_view()),
    path('create_post/', views.PianoCreate.as_view()),
    path('category/<str:slug>/', views.category_page),
    path('<int:pk>/new_comment/', views.new_comment),
    path('', views.PianoList.as_view()),  # shopping/
    path('<int:pk>/', views.PianoDetail.as_view()),  # shopping/1/
]