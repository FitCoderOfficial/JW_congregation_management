from django.urls import path 
from .views import *


app_name = 'display'

urlpatterns = [
    path('reserve/', index, name='reserve'),
]