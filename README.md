# Waitingblock          ![alt text](https://github.com/Waitingblock/Waitingblock/blob/master/waitingblock.svg)
## A Basic Django Waitinglist App built using [django_tables2](https://github.com/jieter/django-tables2), [Bootstrap4](https://getbootstrap.com/)

For development environment, recommend install per [Django Girls Tutorial](https://tutorial.djangogirls.org/en/django_installation/) into the **Waitingblock-master** directory

Install the required dependencies for this project:

```
python3 -m pip install -r requirements.txt
```

Build the database by running all available migrations:

```
python3 manage.py migrate
```

We can set up our local server from the **Waitingblock** directory
```
python manage.py runserver
```

If you'd like to use this in production, please make sure to set the `SECRET_KEY` environment variable, like so:

```
SECRET_KEY=<a_secret_key> python3 manage.py runserver
```
