from django.shortcuts import render
from django.http import HttpResponse

def home_view(request, *args, **kwargs): # *args, **kwargs
    print(args, kwargs)
    print(request.user)
    return render(request, "home.html", {}) #string of HTML code

def contact_view(request, *args, **kwards):
    return render(request, "contact.html", {})

def about_view(request, *args, **kwards):
    my_context={
        "my_text": "This is about us",
        "this_is_true": True,
        "my_number": 123,
        "my_list": ["abc", 4242, 12312],
        "my_html": "<h1>Hello World</h1>",
    }
    return render(request, "about.html", my_context)

def social_view(request, *args, **kwards):
    return HttpResponse("<h1>Social Page</h1>")