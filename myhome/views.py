from django.shortcuts import render

# Create your views here.

def home(request):
    return render(
        request,
        'myhome/home.html'
    )

def my_page(request):
    return render(
        request,
        'myhome/my_page.html'
    )

def about_company(request):
    return render(
        request,
        'myhome/about_company.html'
    )
