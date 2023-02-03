from django.urls import path
from .views import *

urlpatterns = [
    path('congregation-ads/', CongregationAdvertisementListView.as_view(), name='congregation-ads'),
    path('weekday-meetings/', WeekdayMeetingListView.as_view(), name='weekday-meetings'),
    path('appointment-congregation/', AppointmentCongregationListView.as_view(), name='appointment-congregation'),
    path('congregation-group/', CongregationGroupListView.as_view(), name='congregation-group'),
]