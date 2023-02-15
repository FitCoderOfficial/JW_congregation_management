from django.db import models
from accounts.models import JW_User

class Reservation(models.Model):
    user = models.ForeignKey(JW_User, on_delete=models.CASCADE)
    date = models.DateField()
    # add any other fields you need for your reservation, such as a time slot or number of guests

    def __str__(self):
        return f"{self.user} - {self.date}"