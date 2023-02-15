from django.contrib import admin
from django.urls import path
from payments.views import get_session_id, get_item

urlpatterns = [
    path('admin/', admin.site.urls),
    path('buy/<int:item_id>', get_session_id, name='create-checkout-session'),
    path('item/<int:item_id>', get_item)
]

