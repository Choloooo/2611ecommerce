from django.urls import path

from . import views

app_name = "payment"

urlpatterns = [
    path("", views.CartView, name="cart"),
    # path('orderplaced/', views.order_placed, name='order_placed'),
    # path('error/', views.Error.as_view(), name='error'),
    path("orderplaced/", views.order_placed, name="order_placed"),
    path("done/", views.payment_done, name="payment_done"),
]
