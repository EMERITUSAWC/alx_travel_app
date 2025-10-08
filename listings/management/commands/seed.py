from django.core.management.base import BaseCommand
from listings.models import Listing
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = "Seeds the database with sample listings data"

    def handle(self, *args, **options):
        # Prevent duplicate seeding
        if Listing.objects.exists():
            self.stdout.write(self.style.WARNING("Database already seeded."))
            return

        # Create a demo user
        user, _ = User.objects.get_or_create(
            username='demo_user',
            defaults={'email': 'demo@example.com'}
        )

        # Sample listings data
        listings_data = [
            {
                "title": "Luxury Beach Villa",
                "description": "A serene beach villa with ocean views and pool.",
                "location": "Cape Coast",
                "price_per_night": 350.00,
                "available": True,
            },
            {
                "title": "Mountain Retreat Cabin",
                "description": "Quiet cabin with mountain views and hiking trails nearby.",
                "location": "Aburi Hills",
                "price_per_night": 200.00,
                "available": True,
            },
            {
                "title": "City Apartment Suite",
                "description": "Modern apartment in the heart of Accra.",
                "location": "Accra",
                "price_per_night": 180.00,
                "available": True,
            },
        ]

        # Insert listings into the database
        for data in listings_data:
            Listing.objects.create(**data)

        self.stdout.write(
            self.style.SUCCESS("Database successfully seeded with sample listings!")
        )