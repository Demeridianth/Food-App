## venv

create a venv: python -m venv venv
.\venv\Scripts\Activate.ps1

# Django first install
django-admin startproject config .

python manage.py startapp restaurants
python manage.py startapp orders
python manage.py startapp user

# Structure
Models (data structure) (filter for database)
Admin (so you can manage data in Django admin)
Basic views (simple API or pages) (endpoints)
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
-- to enter admin panel -- "http://127.0.0.1:8000/admin/"
-- can fill in DB, newby way

# View (Endpoint) (Change to DRF?? later)
Browser → URL → View → Database → View → Response
A Django view is a Python function that takes a request, talks to the database, and returns a response (JSON or HTML).

# URL's
after url created in app(folder) add it to config/urls
“If URL starts with /api/restaurants/, go check restaurants app”
Connects url(api/restaurants) -> restaurants.urls -> where the view(endpoint) is present -> goes to database

# Fill in DB with real data
1. Admin panel

2. Python django shell:
    python manage.py shell
    from restaurants.models import Restaurant, Dish

    r = Restaurant.objects.create(
    name="Pizza Place",
    address="Main Street 1",
    phone="123456"
)

    Dish.objects.create(
    restaurant=r,
    name="Margherita Pizza",
    price=8.99
)

Dish.objects.create(
    restaurant=r,
    name="Pepperoni Pizza",
    price=10.99
)

    to view data:
    Restaurant.objects.all()
    Dish.objects.all()

3. Load JSON data into DB
    e.x:
    python manage.py loaddata data.json


# to start the app locally
python manage.py runserver


__to_do_next__
finish orders - views, ulrs, etc,
fill in some real data into DB,
