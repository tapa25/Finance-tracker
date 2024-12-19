# Imports
import factory

from apps.tracker.models import Category, Transaction, User


# User Factory
class UserFactory(factory.django.DjangoModelFactory):
    """User Factory

    Inherits:
        factory.django.DjangoModelFactory

    Meta:
        model: apps.tracker.User
        django_get_or_create: ("username", "email", "first_name", "last_name")

    Attributes:
        first_name (str): factory.Faker
        last_name (str): factory.Faker
        username (str): factory.LazyAttribute
        email (str): factory.LazyAttribute
    """

    # Meta Class
    class Meta:
        # Attributes
        model = User
        django_get_or_create = ("username", "email", "first_name", "last_name")

    # Attributes
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    username = factory.LazyAttribute(
        lambda a: f"{a.first_name.lower()}.{a.last_name.lower()}"
    )
    email = factory.LazyAttribute(
        lambda a: f"{a.first_name.lower()}.{a.last_name.lower()}@example.com"
    )


# Category Factory
class CategoryFactory(factory.django.DjangoModelFactory):
    """Category Factory

    Inherits:
        factory.django.DjangoModelFactory

    Meta:
        model: apps.tracker.Category
        django_get_or_create: ("name",)

    Attributes:
        name (str): factory.Iterator
    """

    # Meta Class
    class Meta:
        # Attributes
        model = Category
        django_get_or_create = ("name",)

    # Attributes
    name = factory.Iterator(
        [
            "Food",
            "Transport",
            "Entertainment",
            "Health",
            "Education",
            "Shopping",
            "Utilities",
            "Other",
        ]
    )


# Transaction Factory
class TransactionFactory(factory.django.DjangoModelFactory):
    """Transaction Factory

    Inherits:
        factory.django.DjangoModelFactory

    Meta:
        model: apps.tracker.Transaction
        django_get_or_create: ("name", "amount", "category", "user")
    """

    # Meta Class
    class Meta:
        # Attributes
        model = Transaction
        django_get_or_create = ("user", "category", "type", "amount", "date")

    # Attributes
    user = factory.SubFactory(UserFactory)
    category = factory.SubFactory(CategoryFactory)
    type = factory.Iterator(["INCOME", "EXPENSE"])
    amount = factory.Faker("pydecimal", left_digits=5, right_digits=2, positive=True)
    date = factory.Faker(
        "date_between",
        start_date="-30d",
        end_date="today",
    )
