from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import ContactForm, LoginForm, RegisterForm

def about_page(request):
    return render(request, "home_page.html", {})


def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "Contact",
        "content": "Welcome to the contact page",
        "form": contact_form
    }
    if request.method == "POST":
        print(request.POST)
    if contact_form.is_valid():
        print(contact_form.cleaned_data)

    return render(request, "contact/view.html", context)


def home_page(request):
    return render(request, "home_page.html", {})

def login_page(request):
    login_form = LoginForm(request.POST or None)
    context = {
        "form": login_form
    }
    print("User is logged in")
    #print(request.user.is_authenticated())
    if login_form.is_valid():
        print(login_form.cleaned_data)
        username = login_form.cleaned_data.get("username")
        password = login_form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        #print(request.user.is_authenticated())
        if user is not None:
            print('User is Authentificated: ', request.user.is_authenticated)
            login(request, user)
            print('User is logged in')
            #context['form'] = LoginForm()
            return redirect("/")
        else:
            print("error")

    return render(request, "auth/login.html", context)

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
    return render(request, "auth/register.html", context)
