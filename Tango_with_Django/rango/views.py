from django.shortcuts import render, HttpResponse, redirect
# from django.http import HttpResponse

from .models import Category, Page

from .forms import CategoryForm, PageForm



def index(request):
    # category_list = Category.objects.order_by('-likes')[:5]
    likes = Category.objects.order_by('-likes')[:5]
    views = Page.objects.order_by('-views')[:6]
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


def add_category(request):
    import random
    form = CategoryForm()
    # A HTTP POST?
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            _form = form.save(commit=False)

            _form.views = random.randint(0,100)
            _form.likes = random.randint(0,100)

            _form.save()
            # Now that the category is saved
            # We could give a confirmation message
            # But since the most recent category added is on the index page
            # Then we can direct the user back to the index page.
            return index(request)
    else:
        # The supplied form contained errors -
        # just print them to the terminal.
        print(form.errors)
        # Will handle the bad form, new form, or no form supplied cases.
        # Render the form with error messages (if any).
        return render(request, 'rango/add_category.html', {'form': form})
    

def add_page(request, category_name_slug):
    import random
    try:
        category = Category.objects.get(slug=category_name_slug)

    except Category.DoesNotExist:
        category = None

    form = PageForm()
    
    if request.method == 'POST':
        form = PageForm(request.POST)
        
        if form.is_valid():
            if category:
                page = form.save(commit=False)
                page.category = category
                page.views = random.randint(0,100)
                page.save()
                # return show_category(request, category_name_slug)
                return redirect('show_category', category_name_url=category_name_slug)
                
        else:
            print(form.errors)
            
    context_dict = {'form':form, 'category': category}
    return render(request, 'rango/add_page.html', context_dict)