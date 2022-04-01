from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import request, HttpResponse, JsonResponse
import requests
import datetime
from app.realm_api import BirthdayEmail,WorkAnniversaryEmail


# Create your views here.
def home_page(request):
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

    employee_to_send_emails(employees, configure_employees)

    return render(request, 'app/index.html')


def employee_to_send_emails(employees, configure_employees):
    """ The end date start and end data is not null """
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
    birth_month = (datetime.datetime.strptime((_employee['dateOfBirth'])[:10], "%Y-%m-%d")).strftime('%m')
    birth_day = (datetime.datetime.strptime((_employee['dateOfBirth'])[:10], "%Y-%m-%d")).strftime('%d')

    # Work anniversary
    work_start_month = (datetime.datetime.strptime((_employee['employmentStartDate'])[:10], "%Y-%m-%d")).strftime('%m')
    work_start_day = (datetime.datetime.strptime((_employee['employmentStartDate'])[:10], "%Y-%m-%d")).strftime('%d')

    today = str(datetime.datetime.now())[:10]
    today_month = (datetime.datetime.strptime(today, "%Y-%m-%d")).strftime('%m')
    today_day = (datetime.datetime.strptime(today, "%Y-%m-%d")).strftime('%d')

    if str(birth_month) + '-' + str(birth_day) == str(today_month) + '-' + str(today_day):
        a = BirthdayEmail(name1=_employee['name'], name2=_employee['lastname'])
        a.send_email()

    if str(work_start_month) + '-' + str(work_start_day) == str(today_month) + '-' + str(today_day):
        b = WorkAnniversaryEmail(name1=_employee['name'], name2=_employee['lastname'])
        b.send_email()
