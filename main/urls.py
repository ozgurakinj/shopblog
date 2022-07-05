from django.urls import path
from . import views

urlpatterns = [
path("", views.index, name="index"),
path("products/<slug:slug>", views.products, name="products"),
path("search", views.search, name="search"),
]
