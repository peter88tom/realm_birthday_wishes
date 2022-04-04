from django.core.mail import send_mail
from django.conf import settings


class SendEmail(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def send_email(self):
        print("send email")


class BirthdayEmail(SendEmail):
    def __init__(self, first_name, last_name):
        SendEmail.__init__(self, first_name, last_name)

    def send_email(self):
        # Send email birthday wish
        subject = "Birthday Wish"
        message = f"Happy Birthday {self.first_name} {self.last_name}"
        email_from = "peter88tom@gmail.com"
        email_to = [settings.DEFAULT_FROM_EMAIL]

        try:
            send_mail(subject, message, email_from, email_to)
            # Save to database for tracking purpose
        except Exception as e:
            return "Could not send email"


class WorkAnniversaryEmail(SendEmail):
    def __init__(self, first_name, last_name):
        SendEmail.__init__(self, first_name, last_name)

    def send_email(self):
        print(f"sending work anniversary email {self.first_name} {self.last_name}")

