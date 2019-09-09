Instructions:

Application should run on any machine with python and Django installed.
At the same location as "manage.py" : 'python manage.py runserver'
If output from above command says migrations need to be run : 'python manage.py makemigrations', then 'python manage.py migrate'

navigating to 127.0.0.1:8000 will redirect you to either the Home page or login page based on authentication status.