from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.http import is_safe_url

from .forms import LoginForm, RegisterForm


# Create your views here.
def login_page(request):
    login_form = LoginForm(request.POST or None)
    context = {
        "form": login_form
    }
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None
    if login_form.is_valid():
        username = login_form.cleaned_data.get("username")
        password = login_form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if is_safe_url(redirect_path, request.get_host()):
                return redirect(redirect_path)
            else:
                return redirect("/")
        else:
            print("error")

    return render(request, "accounts/login.html", context)


User = get_user_model()


def register_page(request):
    login_form = RegisterForm(request.POST or None)
    context = {
        "form":login_form
    }
    if login_form.is_valid():
        print(login_form.cleaned_data)

        username  = login_form.cleaned_data.get('username')
        email     = login_form.cleaned_data.get('email')
        password  = login_form.cleaned_data.get('password')
        password2 = login_form.cleaned_data.get('password2')

        new_User = User.objects.create_user(username, email, password)
        print(new_User)
    return render(request, "accounts/register.html", context)

