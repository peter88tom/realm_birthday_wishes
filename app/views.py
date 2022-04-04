"""
In this module will be using python requests library to fetch data from realm employee api
API = https://interview-assessment-1.realmdigital.co.za/
"""
# Django imports
from django.shortcuts import render

# Python module imports
import requests
import datetime

# Custom imports
from app.send_email_birthday_anniversary import BirthdayEmail
from app.models import BirthdayTracker


def employees_api(request):
    employee_end_point = 'https://interview-assessment-1.realmdigital.co.za/employees'
    configure_employee_end_point = 'https://interview-assessment-1.realmdigital.co.za/do-not-send-birthday-wishes'

    all_employee = requests.get(employee_end_point)

    employee_configure = requests.get(configure_employee_end_point)

    if all_employee.status_code == 200:
        employees = all_employee.json()
    else:
        employees = []

    if employee_configure.status_code == 200:
        configure_employees = employee_configure.json()
    else:
        configure_employees = []

    employee_extraction(employees, configure_employees)

    return render(request, 'app/index.html')


def employee_extraction(employees, configure_employees):
    """ Extract a list of employee whose birthdays occur today """
    _employees = []
    for employee in employees:
        # Exclude configured employees
        if employee['id'] in configure_employees:
            pass
        # exclude employees that no longer work and has not started working for realm digital
        else:
            if 'employmentStartDate' in employee and 'employmentEndDate' in employee:
                if employee['employmentStartDate'] is not None and employee['employmentEndDate'] is None and employee['id'] not in configure_employees:
                    send_employee_an_email(employee)
                    _employees.append(employee)

    print(len(_employees))
    return _employees


def send_employee_an_email(_employee):
    # Birthdate
    birth_month = '04' # (datetime.datetime.strptime((_employee['dateOfBirth'])[:10], "%Y-%m-%d")).strftime('%m')
    birth_day = '04' # (datetime.datetime.strptime((_employee['dateOfBirth'])[:10], "%Y-%m-%d")).strftime('%d')

    # Work anniversary
    work_start_month = (datetime.datetime.strptime((_employee['employmentStartDate'])[:10], "%Y-%m-%d")).strftime('%m')
    work_start_day = (datetime.datetime.strptime((_employee['employmentStartDate'])[:10], "%Y-%m-%d")).strftime('%d')

    today = str(datetime.datetime.now())[:10]
    today_month = (datetime.datetime.strptime(today, "%Y-%m-%d")).strftime('%m')
    today_day = (datetime.datetime.strptime(today, "%Y-%m-%d")).strftime('%d')
    send_year = (datetime.datetime.strptime(today, "%Y-%m-%d")).strftime('%Y')

    if str(birth_month) + '-' + str(birth_day) == str(today_month) + '-' + str(today_day):
        # Check if email was send already
        employee_id = _employee['id']
        try:
            BirthdayTracker.objects.get(employee_id=employee_id, email_send_year=send_year)
            print("Email was sent before")
        except BirthdayTracker.DoesNotExist:
            print('Email was not send before, send now')
            birthday_wish = BirthdayEmail(first_name=_employee['name'], last_name=_employee['lastname'],
                                          employee_id=_employee['id'], today=today)
            birthday_wish.send_email()
