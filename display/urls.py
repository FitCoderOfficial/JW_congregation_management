from django.urls import path 
from .views import *


app_name = 'display'

urlpatterns = [
    path('reserve/', index, name='index'),
    path('all_events/', all_events, name='all_events'),
    path('add_event/', add_event, name='add_event'),

]