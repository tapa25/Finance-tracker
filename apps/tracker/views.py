# Imports
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from apps.tracker.models import Transaction


# Index view
def index(request):
    # Render the index.html template
    return render(request, "tracker/index.html")


# Transaction list view
@login_required
def transactions_list(request):
    # Get all transactions for the current user
    transactions = Transaction.objects.filter(user=request.user)

    # Create a context dictionary
    context = {"transactions": transactions}

    # Render the transactions_list.html template
    return render(request, "tracker/transactions_list.html", context)
