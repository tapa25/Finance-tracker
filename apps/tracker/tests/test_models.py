# Imports
import pytest

from apps.tracker.models import Transaction


# Method to test transaction get_expenses method
@pytest.mark.django_db
def test_queryset_get_expenses_method(transactions):
    # Call the function to get the queryset
    queryset = Transaction.objects.get_expenses()

    # Check if the queryset is not empty
    assert queryset.count() > 0

    # Check if all the transactions in the queryset are of type EXPENSE
    assert all([transaction.type == "EXPENSE" for transaction in queryset])


# Method to test transaction get_incomes method
@pytest.mark.django_db
def test_queryset_get_incomes_method(transactions):
    # Call the function to get the queryset
    queryset = Transaction.objects.get_incomes()

    # Check if the queryset is not empty
    assert queryset.count() > 0

    # Check if all the transactions in the queryset are of type INCOME
    assert all([transaction.type == "INCOME" for transaction in queryset])


# Method to test get_total_expenses method
@pytest.mark.django_db
def test_queryset_get_total_expenses_method(transactions):
    # Call the function to get the total expenses
    total_expenses = Transaction.objects.get_total_expenses()

    # Calculate the expected total expenses
    expected_total_expenses = sum(
        [
            transaction.amount
            for transaction in transactions
            if transaction.type == "EXPENSE"
        ]
    )

    # Check if the total expenses are correct
    assert total_expenses == expected_total_expenses


# Method to test get_total_incomes method
@pytest.mark.django_db
def test_queryset_get_total_incomes_method(transactions):
    # Call the function to get the total incomes
    total_incomes = Transaction.objects.get_total_incomes()

    # Calculate the expected total incomes
    expected_total_incomes = sum(
        [
            transaction.amount
            for transaction in transactions
            if transaction.type == "INCOME"
        ]
    )

    # Check if the total incomes are correct
    assert total_incomes == expected_total_incomes
