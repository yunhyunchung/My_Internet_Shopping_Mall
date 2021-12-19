from django.shortcuts import render
from shopping.models import Piano

def landing(request):
    recent_pianos = Piano.objects.order_by('-pk')[:3]
    return render(request, 'myhome/landing.html',
                  {'recent_pianos': recent_pianos})

def my_page(request):
    commented_pianos = Piano.objects.all()
    return render(
        request, 'myhome/my_page.html',
        {'commented_pianos': commented_pianos})

def about_company(request):
    return render(
        request,
        'myhome/about_company.html'
    )
