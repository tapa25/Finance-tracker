# Imports
import pytest
from django.contrib.humanize.templatetags.humanize import intcomma
from django.urls import reverse


# Function to test the total values on transactions_list view
@pytest.mark.django_db
def test_total_values_appear_on_transactions_list_page(user_transactions, client):
    # Unpack the user and the transactions
    user, transactions = user_transactions

    # Login the user
    client.force_login(user)

    # Get the total income and expense and calculate the net income
    total_income = sum([t.amount for t in transactions if t.type == "INCOME"])
    total_expense = sum([t.amount for t in transactions if t.type == "EXPENSE"])
    net_income = total_income - total_expense

    # Get the response from the transactions_list view
    response = client.get(reverse("tracker:transactions_list"))

    # Check if the total income, expense and net income are in the context
    assert response.context["total_income"] == total_income
    assert response.context["total_expense"] == total_expense
    assert response.context["net_income"] == net_income

    # Check if the total income, expense and net income are in the response
    assert intcomma(total_income) in response.content.decode()
    assert intcomma(total_expense) in response.content.decode()
    assert intcomma(net_income) in response.content.decode()
