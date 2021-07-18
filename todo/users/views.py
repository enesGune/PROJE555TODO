from django.shortcuts import render

# Create your views here.


def login_user(request, *args, **kwargs):
    return render(request, "login.html", {})
