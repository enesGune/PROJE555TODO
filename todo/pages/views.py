from django.shortcuts import render

# Create your views here.


def login_page(request, *args, **kwargs):
    return render(request, "login.html", {})


def dasboard_page(request, *args, **kwargs):
    return render(request, "dasboard.html", {})
