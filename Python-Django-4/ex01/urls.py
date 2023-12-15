from django.urls import path
from ex01 import views


#Path donde está el template
urlpatterns = [
    path('', views.history, name='history'),
]