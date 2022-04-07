from django import views
from django.urls import path
from . import views
urlpatterns = [
    path('register/',views.register),
    path('logout/',views.logout_user),
]
