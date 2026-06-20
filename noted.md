## venv

create a venv: python -m venv venv
.\venv\Scripts\Activate.ps1

# Django first install
django-admin startproject config .

python manage.py startapp restaurants
python manage.py startapp orders
python manage.py startapp user

# Structure
Models (data structure)
Admin (so you can manage data in Django admin)
Basic views (simple API or pages)
URLs wiring

# Migrations
python manage.py makemigrations restaurants ----checks the models and creates migrationsinstructions for the db
python manage.py migrate --actually creates tables etc. (by default in db.sqlite)

1. change models.py
2. python manage.py makemigrations
3. python manage.py migrate

# Admin panel
python manage.py createsuperuser --login creds creation
python manage.py runserver --run local

# View (Endpoint) (Change to DRF?? later)
Browser → URL → View → Database → View → Response
A Django view is a Python function that takes a request, talks to the database, and returns a response (JSON or HTML).

# URL's
after url created in app(folder) add it to config/urls
“If URL starts with /api/restaurants/, go check restaurants app”
Connects url(api/restaurants) -> restaurants.urls -> where the view is present -> goes to database

# to start the app locally
python manage.py runserver


__to_do_next__
finish restaurants,
fill in some real data into DB,
move on to orders, try as much as yourself