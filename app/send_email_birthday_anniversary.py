from django.core.mail import send_mail
from django.conf import settings
from app.models import BirthdayTracker
import datetime


class SendEmail(object):
    def __init__(self, first_name, last_name, employee_id, today):
        self.first_name = first_name
        self.last_name = last_name
        self.employee_id = employee_id
        self.today = today

    def send_email(self):
        print("send email")


class BirthdayEmail(SendEmail):
    def __init__(self, first_name, last_name, employee_id, today):
        SendEmail.__init__(self, first_name, last_name, employee_id, today)

    def send_email(self):
        # Send email birthday wish
        subject = "Birthday Wish"
        message = f"Happy Birthday {self.first_name} {self.last_name}"
        email_from = "peter88tom@gmail.com"
        email_to = [settings.DEFAULT_FROM_EMAIL]

        try:
            send_mail(subject, message, email_from, email_to)

            # Save to database for tracking purpose
            new_record = BirthdayTracker()
            new_record.employee_id = self.employee_id
            new_record.email_send = True
            new_record.email_send_year = (datetime.datetime.strptime(self.today, "%Y-%m-%d")).strftime('%Y')
            new_record.email_send_day = (datetime.datetime.strptime(self.today, "%Y-%m-%d")).strftime('%m')

            new_record.save()
        except Exception as e:
            print(e)
            return "Could not send email"
