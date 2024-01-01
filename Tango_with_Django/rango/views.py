from django.shortcuts import render, HttpResponse
# from django.http import HttpResponse

# Create your views here.

def index(request):
    context = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
    
    return render(request, 'rango/index.html', context=context)

def about(request):
    text = '''
    Rango says here is the about page.
    <a href="/rango/">back</a>
'''
    return HttpResponse(text)