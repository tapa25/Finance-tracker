# Imports
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from apps.tracker.filters import TransactionFilter
from apps.tracker.models import Transaction


# Index view
def index(request):
    """Index view

    Args:
        request (HttpRequest): The request object

    Returns:
        HttpResponse: The response object
    """

    # Render the index.html template
    return render(request, "tracker/index.html")


# Transaction list view
@login_required
def transactions_list(request):
    """Transaction list view

    Args:
        request (HttpRequest): The request object

    Returns:
        HttpResponse: The response object
    """

    # Create a transaction filter
    transaction_filter = TransactionFilter(
        data=request.GET,
        queryset=Transaction.objects.filter(user=request.user).select_related(
            "category"
        ),
    )

    # Get the total income and total expense
    total_income = transaction_filter.qs.get_total_income() or 0
    total_expense = transaction_filter.qs.get_total_expense() or 0

    # Create a context dictionary
    context = {
        "filter": transaction_filter,
        "total_income": total_income,
        "total_expense": total_expense,
        "net_income": total_income - total_expense,
    }

    # Check if the request is htmx request
    if request.htmx:
        # Render the transactions_container.html template
        return render(
            request, "tracker/components/transactions_container.html", context
        )

    # Render the transactions_list.html template
    return render(request, "tracker/transactions_list.html", context)
