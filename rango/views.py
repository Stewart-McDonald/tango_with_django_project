from django.shortcuts import render
from rango.models import Category
from rango.models import Page
from rango.forms import CategoryForm
from rango.forms import PageForm


def index(request):
    category_list = Category.objects.order_by("-likes")[:5]
    page_list = Page.objects.order_by('-views')[:5]
    print(category_list, page_list)
    context_dict = {'categories': category_list, 'pages': page_list}
    return render(request, 'rango/index.html', context=context_dict)

# Return a rendered response to send to the client.
# We make use of the shortcut function to make our lives easier.
# Note that the first parameter is the template we wish to use.


def about(request):
    context_dict = {}
    return render(request, 'rango/about.html', context =context_dict)


def show_category(request, category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None
    return render(request, 'rango/category.html', context_dict)


def add_category(request):
    form = CategoryForm()
    # A HTTP POST? POST submits data from client to server for processing.
    # A HTTP GET is used to request a representation of the specified resource. In other
    # words, we use a HTTP GET to retrieve a particular resource, whether it is a web page,

    # image or other file.
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            # Now that the category is saved
            # We could give a confirmation message
            # But since the most recent category added is on the index page
            # Then we can direct the user back to the index page
            return index(request)
        else:
            print("form errors are: ", form.errors)
    return render(request, 'rango/add_category.html', {'form': form})


def add_page(request, category_name_slug):
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
                page.views = 0
                page.save()
                return show_category(request, category_name_slug)
        else:
            print(form.errors)
    context_dict = {'form': form, 'category': category}
    return render(request, 'rango/add_page.html', context_dict)
