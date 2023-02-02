from django.urls import path
from .views import CongregationAdvertisementListView, WeekdayMeetingListView, AppointmentCongregation

urlpatterns = [
    path('congregation-ads/', CongregationAdvertisementListView.as_view(), name='congregation-ads'),
    path('weekday-meetings/', WeekdayMeetingListView.as_view(), name='weekday-meetings'),
    path('appointment-congregation/', AppointmentCongregation.as_view(), name='appointment-congregation'),
]