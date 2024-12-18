# Imports
import random

from django.core.management.base import BaseCommand
from faker import Faker

from apps.tracker.models import Category, Transaction, User


# Create command class
class Command(BaseCommand):
    """generate_transactions Command

    Insert random transactions for all users in the database

    Inherits:
        Base

    Attributes:
        help (str): "Generate random transactions for all users"

    Methods:
        handle: Handle method
    """

    # Help message
    help = "Generate random transactions for all users"

    # Add arguments
    def add_arguments(self, parser):
        # Argument for number of transactions
        parser.add_argument(
            "--num-transactions",
            type=int,
            default=20,
            help="Number of transactions to generate",
        )

    # Handle method
    def handle(self, *args, **kwargs):
        # Notify about start
        self.stdout.write(self.style.WARNING("Generating transactions..."))

        # Initialize Faker
        fake = Faker()

        # List to store categories
        categories = [
            "Bills",
            "Food",
            "Clothes",
            "Medical",
            "Housing",
            "Salary",
            "Social",
            "Transport",
            "Vacation",
        ]

        # Ensure categories exist in the database
        category_objects = []

        # Traverse over the categories
        for category in categories:
            # Create a new category (use get_or_create to avoid duplicates)
            category_obj, _ = Category.objects.get_or_create(name=category)

            # Add the category to the list
            category_objects.append(category_obj)

        # Get existing users count
        existing_users_count = User.objects.filter(is_staff=False).count()

        # If less than 5 users exist, create more
        if existing_users_count < 5:
            # Traverse over range of users to create
            for _ in range(5 - existing_users_count):
                # Create a new user
                User.objects.create_user(
                    username=fake.user_name(),
                    email=fake.email(),
                    first_name=fake.first_name(),
                    last_name=fake.last_name(),
                    password="demo@1234",
                )

        # Get all non-admin users
        users = User.objects.filter(is_staff=False)

        # Get all transaction types
        transaction_types = [
            choice[0] for choice in Transaction.TRANSACTION_TYPE_CHOICES
        ]

        # Traverse over users
        for user in users:
            # Get number of transactions to generate
            num_transactions = kwargs["num_transactions"]

            # Traverse over range of transactions
            for _ in range(num_transactions):
                # Create a new transaction
                Transaction.objects.create(
                    user=user,
                    category=random.choice(category_objects),
                    type=random.choice(transaction_types),
                    amount=random.uniform(250, 2500),
                    date=fake.date_this_year(before_today=True),
                )

        # Notify about completion
        self.stdout.write(
            self.style.SUCCESS(
                f"Generated {kwargs['num_transactions']} transactions for {len(users)} users."
            )
        )
