# ALX Travel App - Milestone 2

Models, serializers, and database seeder for a travel booking app.

## Features

- `Listing`, `Booking`, `Review` models
- DRF serializers
- Seeder command: `python manage.py seed`

## Setup

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py seed
python manage.py runserver