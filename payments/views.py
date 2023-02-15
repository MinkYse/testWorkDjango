from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.http import JsonResponse
from .models import Item

import stripe


def get_session_id(request, item_id):
    if request.method == 'GET':
        domain = request.build_absolute_uri('/')[:-1]
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
            success_url=domain,
            cancel_url=domain,
        )
        return JsonResponse({'id': checkout_session.id})


def get_item(request, item_id):
    if request.method == 'GET':
        item = get_object_or_404(Item, pk=item_id)
        if item.currency == 'usd':
            pub = settings.STRIPE_PUBLIC_KEY_USD
        else:
            pub = settings.STRIPE_PUBLIC_KEY_RUB
        context = {
            'item': item,
            'stripe_public_key': pub
        }
        return render(request, 'item.html', context)
