# Problem definition
Design and implement a service component that will send birthday wishes to employees.

The service must extract a list of employees whose birthdays occur today using the Realm Digital Employee API
and create a generic message E.g. “Happy Birthday {name 1}, {name 2}” and send the message to an email
address configured for the component.

# Running this project
To get this project up and running you should start by having latest Python installed on your computer. Install virtual environment in your computer like this
```
pip install virtualenv
```

Clone or download this repository and open it in your editor of choice. In a terminal (mac/linux) or windows terminal, run the following command in the base directory of this project

```
virtualenv env
```

That will create a new folder `env` in your project directory. Next activate it with this command on mac/linux:

```
source env/bin/active
```

Then install the project dependencies with

```
pip install -r requirements.txt
```


Now you can run the project with this command

```
python manage.py runserver
```
