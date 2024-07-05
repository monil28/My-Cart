from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name='ShopHome'),
    path("about/", views.about, name='about')
]