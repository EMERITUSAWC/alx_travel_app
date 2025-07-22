from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from listings.models import Listing


class Command(BaseCommand):
    help = 'Seeds the database with sample listings'

    def handle(self, *args, **options):
        user, created = User.objects.get_or_create(
            username='admin',
            defaults={'is_staff': True, 'is_superuser': True, 'email': 'admin@example.com'}
        )
        if created:
            user.set_password('admin')
            user.save()
            self.stdout.write(self.style.WARNING('Created admin user with password "admin"'))

        sample_listings = [
            {
                "title": "Cozy Beach Cottage",
                "description": "A charming cottage near the beach with ocean views.",
                "location": "Malibu",
                "price_per_night": 150.00,
                "bedrooms": 2,
                "max_guests": 4
            },
            {
                "title": "Modern Downtown Loft",
                "description": "Stylish loft in the heart of the city.",
                "location": "New York",
                "price_per_night": 250.00,
                "bedrooms": 1,
                "max_guests": 2
            },
            {
                "title": "Mountain Cabin Retreat",
                "description": "Peaceful cabin surrounded by nature and forests.",
                "location": "Aspen",
                "price_per_night": 200.00,
                "bedrooms": 3,
                "max_guests": 6
            },
            {
                "title": "Luxury Penthouse Suite",
                "description": "Elegant penthouse with panoramic skyline views.",
                "location": "Chicago",
                "price_per_night": 400.00,
                "bedrooms": 2,
                "max_guests": 4
            },
            {
                "title": "Rustic Farmhouse Stay",
                "description": "Authentic countryside experience on a working farm.",
                "location": "Napa Valley",
                "price_per_night": 180.00,
                "bedrooms": 4,
                "max_guests": 8
            }
        ]

        created_count = 0
        for item in sample_listings:
            listing, created = Listing.objects.get_or_create(
                title=item["title"],
                defaults={
                    "description": item["description"],
                    "location": item["location"],
                    "price_per_night": item["price_per_night"],
                    "bedrooms": item["bedrooms"],
                    "max_guests": item["max_guests"]
                }
            )
            if created:
                created_count += 1

        self.stdout.write(
            self.style.SUCCESS(f'Successfully seeded {created_count} new listings.')
        )