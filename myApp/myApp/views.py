from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from .forms import ContactForm


def about_page(request):
    return render(request, "home_page.html", {})


def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "Contact",
        "content": "Welcome to the contact page",
        "form": contact_form
    }
    # if request.method == "POST":
    #     print(request.POST)
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
        if request.is_ajax():
            return JsonResponse({"message": "Thank you for your submission"})

    if contact_form.errors:
        errors = contact_form.errors.as_json()
        if request.is_ajax():
            return HttpResponse(errors, status=400, content_type='application/json')
    return render(request, "contact/view.html", context)


def home_page(request):
    print(request.session.get("first_name", "Unknown"))
    return render(request, "home_page.html", {})


