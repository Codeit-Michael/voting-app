from django.urls import path
from . import views

urlpatterns = [
    path('newline/',views.func1)
]