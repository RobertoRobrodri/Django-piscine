from django.urls import path
from ex00 import views

urlpatterns = [
    path('', views.members, name='members'),
]