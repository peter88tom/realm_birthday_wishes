from django.db import models


# This table will store employee id and year
class BirthdayTracker(models.Model):
    employee_id = models.IntegerField()
    email_send = models.BooleanField(default=False)
    email_send_year = models.IntegerField()
    email_send_day = models.IntegerField()

    def __str__(self):
        return f"employee_id:{self.employee_id} "
