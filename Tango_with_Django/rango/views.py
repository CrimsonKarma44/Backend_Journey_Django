from django.shortcuts import render, HttpResponse
# from django.http import HttpResponse
from .models import Category, Page

# Create your views here.

def index(request):
    # category_list = Category.objects.order_by('-likes')[:5]
    likes = Category.objects.order_by('-likes')
    views = Page.objects.order_by('-views')
    context = {
        # 'categories': category_list,
        'likes': likes,
        'views': views
        }
    
    return render(request, 'rango/index.html', context=context)

def about(request):
    context = {'name': "Vincent Princewill"}
    
    return render(request, 'rango/about.html', context=context)

def show_category(request, category_name_url):
    context = {}
    try:
        category = Category.objects.get(slug=category_name_url)
        pages = Page.objects.filter(category=category)
        

        context['pages'] = pages
        context['category'] = category

    except Category.DoesNotExist:
        context['category'] = None
        context['pages'] = None

    return render(request, 'rango/category.html', context)