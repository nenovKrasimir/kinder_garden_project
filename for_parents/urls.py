from django.urls import path
from . import views

urlpatterns = [
    path('', views.for_parents, name='for_parents'),
]