from django.urls import path 
from .views import *


app_name = 'display'

urlpatterns = [
    path('reserve/', reserve, name='reserve'),
]