from django.shortcuts import render
from django.views.generic import ListView
from .models import *

class CongregationAdvertisementListView(ListView):
    model = CongregationAdvertisement
    template_name = 'congregation_ads.html'
    context_object_name = 'congregation_ads'

class WeekdayMeetingListView(ListView):
    model = WeekdayMeeting
    template_name = 'weekday_meetings.html'
    context_object_name = 'weekday_meetings'

class AppointmentCongregationListView(ListView):
    model = AppointmentCongregation
    template_name = 'appointment_congregation.html'
    context_object_name = 'appointment_congregation'

class CongregationGroupListView(ListView):
    model = CongregationGroup
    template_name = 'congregation_group.html'
    context_object_name = 'congregation_group'