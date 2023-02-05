from django.urls import path
from .views import *

urlpatterns = [
    path('', MagazineListView.as_view(), name='magazine_list'),
    path('<int:pk>/', MagazineDetailView.as_view(), name='magazine_detail'),
    path('subscriptions/', SubscriptionListView.as_view(), name='subscription_list'),
]