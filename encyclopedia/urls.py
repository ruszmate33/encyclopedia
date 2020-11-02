from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("WIKI/<str:title>", views.entry, name="entry"),
    path("search", views.search, name="search")
]
