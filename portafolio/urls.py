from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_portafolio, name='home-portafolio'),
]