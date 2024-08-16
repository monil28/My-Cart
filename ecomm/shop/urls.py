from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='ShopHome'),
    path("about/", views.about, name='about'),
    path("contact/", views.contact, name='contact'),
    path("products/<int:product_id>", views.productview, name='productview'),
    path("checkout/", views.checkout, name='checkout')
]
