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


# Method to test get_total_expense method
@pytest.mark.django_db
def test_queryset_get_total_expense_method(transactions):
    # Call the function to get the total expense
    total_expense = Transaction.objects.get_total_expense()

    # Calculate the expected total expense
    expected_total_expense = sum(
        [
            transaction.amount
            for transaction in transactions
            if transaction.type == "EXPENSE"
        ]
    )

    # Check if the total expense are correct
    assert total_expense == expected_total_expense


# Method to test get_total_income method
@pytest.mark.django_db
def test_queryset_get_total_income_method(transactions):
    # Call the function to get the total income
    total_income = Transaction.objects.get_total_income()

    # Calculate the expected total income
    expected_total_income = sum(
        [
            transaction.amount
            for transaction in transactions
            if transaction.type == "INCOME"
        ]
    )

    # Check if the total income are correct
    assert total_income == expected_total_income
