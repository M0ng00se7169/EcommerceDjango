from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.utils.http import is_safe_url

import stripe
stripe.api_key = "sk_test_uASrisECxtnSTKbC5nvbODeF"
STRIPE_PUBLISH_KEY = "pk_test_WmBcmvNaiIUJxzw3wjKxG8mK"


def payment_method_view(request):
    next_url = None
    next_ = request.GET.get('next')
    if is_safe_url(next_, request.get_host()):
        next_url = next_

    return render(request, 'billing/payment-method.html', {"publish_key": STRIPE_PUBLISH_KEY, "next_url": next_url})


def payment_method_create_view(request):
    if request.method == 'POST' and request.is_ajax():
        print(request.POST)
        return JsonResponse({"message": "Success! Your card was added."})
    raise HttpResponse("error", status_code=401)
