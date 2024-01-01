from django.shortcuts import render, HttpResponse
# from django.http import HttpResponse

# Create your views here.

def index(request):
    context = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
    
    return render(request, 'rango/index.html', context=context)

def about(request):
    context = {'name': "Vincent Princewill"}
    
    return render(request, 'rango/about.html', context=context)
