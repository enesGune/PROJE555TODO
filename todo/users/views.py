from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def login_user(request, *args, **kwargs):
    return render(request, "login.html", {})


def login_view(request):
    form = LoginForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data('username')
        password = form.cleaned_data('password')
        user = authenticate(
            request,
            username=username,
            password=password,
        )

        if user == None:
            request.session['invalid-user'] = 1
            return render(
                request,
                "login.html",
                {
                    "form": form,
                }
            )
        else:
            login(request, user)
            return redirect("/")

    return render(
        request,
        "login.html",
        {
            "form": form,
        }
    )
