from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('za_nas', views.about_us, name='about_us')
]