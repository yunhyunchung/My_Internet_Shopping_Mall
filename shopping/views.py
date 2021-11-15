# from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Piano

# 상품 목록 페이지
class PianoList(ListView):
    model = Piano
    ordering = '-pk'

# 상품 상세 페이지
class PianoDetail(DetailView):
    model = Piano

