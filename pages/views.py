from django.shortcuts import render
from django.http import HttpResponse


def home_view(request, *args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)
    print("request:", request)
    print("request.user:", request.user)
    # return HttpResponse("<h1>Hello world</h1>")
    return render(request, "home.html", {})


def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})


def about_view(request, *args, **kwargs):
    my_context = {
        "my_text": "This is about us",
        "my_number": 123,
        "my_list": [1, 3, 5, 7, 11, "abc"],
        "my_html": "<h4>Some HTML</h4>"
    }
    return render(request, "about.html", my_context)
