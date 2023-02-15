from django.contrib import admin
from django.urls import path
from payments.views import get_item, get_stripe_payments

urlpatterns = [
    path('admin/', admin.site.urls),
    path('buy/<int:item_id>', get_stripe_payments, name='create-payment-intent'),
    path('item/<int:item_id>', get_item),
]

