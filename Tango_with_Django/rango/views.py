from django.shortcuts import render, HttpResponse
# from django.http import HttpResponse
from .models import Category, Page

# Create your views here.

def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    context = {'categories': category_list}
    
    return render(request, 'rango/index.html', context=context)

def about(request):
    context = {'name': "Vincent Princewill"}
    
    return render(request, 'rango/about.html', context=context)
    
def show_category(request):
    pass