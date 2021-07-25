from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout, get_user_model
# Create your views here.

User = get_user_model()


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


def logout_view(request):
    logout(request)
    return redirect("/login")


def register_view(request):
    form = RegisterForm(request.POST or None)

    if form.is_valid():

        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password1")
        password2 = form.cleaned_data.get("password2")
        try:
            user = User.objects.create_user(username, email, password)
        except:
            user = None
        if user != None:
            login(request, user)
            return redirect("/")
        else:
            request.session['register_error'] = 1

    return render(request, "login.html", {"form": form})
