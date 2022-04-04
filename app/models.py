from django.db import models


# Create your models here.
class BirthdayTracker(models.Model):
    employee_id = models.IntegerField()
    email_send = models.BooleanField(default=False)

    def __str__(self):
        return self.employee_id
