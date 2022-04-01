class SendEmail(object):
    def __init__(self, name1, name2):
        self.name1 = name1
        self.name2 = name2

    def send_email(self):
        print("send email")


class BirthdayEmail(SendEmail):
    def __init__(self, name1, name2, email="peter88tom@gmail.com"):
        self.email = email
        SendEmail.__init__(self, name1, name2)

    def send_email(self):
        print(f"sending birthday with {self.name1} {self.name2} to {self.email}")


class WorkAnniversaryEmail(SendEmail):
    def __init__(self, name1, name2):
        SendEmail.__init__(self, name1, name2)

    def send_email(self):
        print(f"sending work anniversary email {self.name1} {self.name2}")

