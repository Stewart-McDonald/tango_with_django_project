from django.shortcuts import render


def index(request):
    context_dict = {'boldmessage':"Crunchy, creamy, cookie, candy, cupcake!"}
    return render(request, 'rango/index.html', context=context_dict)

# Return a rendered response to send to the client.
# We make use of the shortcut function to make our lives easier.
# Note that the first parameter is the template we wish to use.


def about(request):
    context_dict = {}
    return render(request, 'rango/about.html', context =context_dict)

