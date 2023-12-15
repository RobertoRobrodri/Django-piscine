from django.urls import path
from ex02 import views


#Path donde está el template
urlpatterns = [
    path('', views.login, name='login'),
]