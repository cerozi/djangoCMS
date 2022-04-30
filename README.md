# Django CUSTOMER MANAGEMENT SYSTEM

A customer management system made using Django 3.2.10 and Python 3.7.6. Contains simple CRUD operations, user profiles, permissions and simple django signals features. You can find the deploy project at https://cms-with-django.herokuapp.com/. (login: admin - password: admin)

# To run this project...

Clone this repo:
```python
git clone https://github.com/cerozi/djangoblog.git
```

With your virtual enviroment on, install all packages and modules found in requirements.txt:
```python
pip install requirements.txt
```

Make the database migrations:

```
python manage.py makemigrations
python manage.py migrate
```

Now, run the server and the project can be found on your localhost (http://127.0.0.1:8000/):
```python
python manage.py runserver
```
