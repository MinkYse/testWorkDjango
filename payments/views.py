from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.http import JsonResponse
from .models import Item

import json

import stripe


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


def get_stripe_payments(request, item_id):
    try:
        item = get_object_or_404(Item, pk=item_id)
        if item.currency == 'usd':
            stripe.api_key = settings.STRIPE_SECRET_KEY_USD
        else:
            stripe.api_key = settings.STRIPE_SECRET_KEY_RUB
        intent = stripe.PaymentIntent.create(
            amount=item.price,
            currency=item.currency,
            metadata={
                "product_id": item.id
            }
        )
        return JsonResponse({
            'clientSecret': intent['client_secret']
        })
    except Exception as e:
        return JsonResponse({'error': str(e)})
