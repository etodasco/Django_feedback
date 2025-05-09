from django.urls import path, include
from . import views

urlspattern = {
    path("", views.review),
    path("", include("reviews.urls"))
}