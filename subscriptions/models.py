# subscriptions/models.py

from django.db import models
from accounts.models import JW_User

class Magazine(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='magazine_images/')
    quantity = models.PositiveIntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Subscription(models.Model):
    user = models.ForeignKey(JW_User, on_delete=models.CASCADE)
    magazine = models.ForeignKey(Magazine, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} subscribed to {self.magazine.name}"