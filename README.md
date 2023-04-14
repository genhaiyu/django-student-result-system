# django-student-result-system

> Tutoring project - education purpose


## Documentation

1.1. The project dedicated to my student, it from online open-source projects.


1.2. How to run (Python 3.11)

* python -m pip install -r requirements.txt
* sudo pip3 install virtualenv
    * virtualenv venv
    * source venv/bin/activate
* python manage.py migrate
* python manage.py createsuperuser
* python manage.py runserver

1.3. Optional, if runserver is caused by `cryptography` problem.

* python -m pip uninstall cryptography
* python -m pip install cryptography

<img src="./chart/basic-django.png" alt="chart" width="350">


## License
[![GNU General Public License v3.0](https://img.shields.io/github/license/genhaiyu/django-student-result-system)](https://github.com/genhaiyu/django-student-result-system/blob/master/LICENSE)
