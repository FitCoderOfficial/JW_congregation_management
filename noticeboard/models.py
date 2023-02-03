from django.db import models

class CongregationAdvertisement(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='congregation_ads/')
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class WeekdayMeeting(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='weekday_meetings/')
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class AppointmentCongregation(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='weekend_meetings/')
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class CongregationGroup(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='congregation_group/')
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.name