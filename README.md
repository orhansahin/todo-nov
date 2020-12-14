# todo-nov

## Installation & Run Guide

1. Clone repository
2. *(Optional)* Using virtualenv
    ```
    pip3 install virtualenv
    virtualenv --python=python3 env
    source env/bin/activate
    ```
3. cd into repository
4. `pip3 install -r requirements.txt`

5. `python manage.py migrate`
6. `python manage.py runserver`

7. To create superuser execute:
   `python manage.py createsuperuser`
