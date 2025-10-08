from django.core.management.base import BaseCommand
from listings.models import Listing
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = "Seed the database with sample listings data"

    def handle(self, *args, **kwargs):
        if Listing.objects.exists():
            self.stdout.write(self.style.WARNING("Listings already exist. Skipping seeding."))
            return

        # Ensure a test user exists
        user, created = User.objects.get_or_create(username="testuser")
        if created:
            user.set_password("password123")
            user.save()

        sample_listings = [
            {
                "title": "Beachside Villa",
                "description": "A beautiful villa near the ocean.",
                "location": "Miami",
                "price_per_night": 250.00
            },
            {
                "title": "Mountain Cabin",
                "description": "Cozy cabin in the mountains.",
                "location": "Colorado",
                "price_per_night": 150.00
            },
            {
                "title": "City Apartment",
                "description": "Modern apartment in the city center.",
                "location": "New York",
                "price_per_night": 200.00
            },
        ]

        for data in sample_listings:
            Listing.objects.create(**data)

        self.stdout.write(self.style.SUCCESS("Database seeded successfully with sample listings!"))
