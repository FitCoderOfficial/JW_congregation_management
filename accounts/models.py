from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save

POSITION_CHOICES = [
    ('전도인', '전도인'),
    ('봉사의종', '봉사의종'),
    ('장로', '장로'),
]

STATUS_CHOICES = [
    ('대기', '대기'),
    ('승인', '승인'),
    ('거절', '거절'),
]

class JW_User(AbstractUser):
    mobile_number = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True, default='default.jpg')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='봉사의종')
    role = models.CharField(max_length=10, choices=POSITION_CHOICES, default='장로')

@receiver(post_save, sender=JW_User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        instance.status = '대기'
        instance.role = '전도인'
        instance.save()