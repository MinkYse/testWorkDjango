from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.http import JsonResponse
from .models import Item

import stripe

# Create your views here.


YOUR_DOMAIN = "http://127.0.0.1:8000"


def get_session_id(request, item_id):
    if request.method == 'GET':
        item = get_object_or_404(Item, pk=item_id)
        if item.currency == 'usd':
            stripe.api_key = settings.STRIPE_SECRET_KEY_USD
        else:
            stripe.api_key = settings.STRIPE_SECRET_KEY_RUB
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': item.currency,
                        'unit_amount': item.price,
                        'product_data': {
                            'name': item.name
                        },
                    },
                    'quantity': 1,
                },
            ],
            metadata={
                'item_id': item.id
            },
            mode='payment',
            success_url=YOUR_DOMAIN + '/success/',
            cancel_url=YOUR_DOMAIN + '/cancel/',
        )
        return JsonResponse({'id': checkout_session.id})


def get_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if item.currency == 'usd':
        pub = settings.STRIPE_PUBLIC_KEY_USD
    else:
        pub = settings.STRIPE_PUBLIC_KEY_RUB
    print(settings.ROOT)
    context = {
        'item': item,
        'stripe_public_key': pub
    }
    return render(request, 'item.html', context)