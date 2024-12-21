# Imports
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_http_methods
from django_htmx.http import retarget
from tablib import Dataset

from apps.tracker.charts import plot_category_pie_chart, plot_income_expense_bar_chart
from apps.tracker.filters import TransactionFilter
from apps.tracker.forms import TransactionForm
from apps.tracker.models import Transaction
from apps.tracker.resources import TransactionResource


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

    # Paginate the transactions
    paginator = Paginator(transaction_filter.qs, settings.PAGE_SIZE)

    # Get the page from the request
    transaction_page = paginator.get_page(1)

    # Get the total income and total expense
    total_income = transaction_filter.qs.get_total_income() or 0
    total_expense = transaction_filter.qs.get_total_expense() or 0

    # Create a context dictionary
    context = {
        "transactions": transaction_page,
        "filter": transaction_filter,
        "total_income": total_income,
        "total_expense": total_expense,
        "net_income": total_income - total_expense,
    }

    # Check if the request is htmx request
    if request.htmx:
        # Render the transactions_container.html template
        return render(request, "tracker/partials/transactions_container.html", context)

    # Render the transactions_list.html template
    return render(request, "tracker/transactions_list.html", context)


# Transaction create view
@login_required
def transaction_create(request):
    """Transaction create view

    Args:
        request (HttpRequest): The request object

    Returns:
        HttpResponse: The response object
    """

    # If request is POST
    if request.method == "POST":
        # Create a transaction form
        form = TransactionForm(request.POST)

        # Check if the form is valid
        if form.is_valid():
            # Save the form
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()

            # Create a context dictionary
            context = {"message": "Transaction created successfully!"}

            # Render the transaction_success.html template
            return render(request, "tracker/partials/transaction_success.html", context)

        # If the form is not valid
        else:
            # Create a context dictionary
            context = {"form": form}

            # Create a response object
            response = render(
                request, "tracker/partials/transaction_create.html", context
            )

            # Return the retarget response
            return retarget(response, "#transaction-block")

    # Create a context dictionary
    context = {"form": TransactionForm()}

    # Render the transaction_create.html template
    return render(request, "tracker/partials/transaction_create.html", context)


# Transaction update view
@login_required
def transaction_update(request, pk):
    """Transaction update view

    Args:
        request (HttpRequest): The request object
        pk (int): The primary key of the transaction

    Returns:
        HttpResponse: The response object
    """

    # Get the transaction object for the authenticated user
    transaction = get_object_or_404(Transaction, pk=pk, user=request.user)

    # If the request is POST
    if request.method == "POST":
        # Create a transaction form
        form = TransactionForm(request.POST, instance=transaction)

        # Check if the form is valid
        if form.is_valid():
            # Save the form
            form.save()

            # Create a context dictionary
            context = {"message": "Transaction updated successfully!"}

            # Render the transaction_success.html template
            return render(request, "tracker/partials/transaction_success.html", context)

        # If the form is not valid
        else:
            # Create a context dictionary
            context = {
                "form": form,
                "transaction": transaction,
            }

            # Create a response object
            response = render(
                request, "tracker/partials/transaction_update.html", context
            )

            # Return the retarget response
            return retarget(response, "#transaction-block")

    # Create a context dictionary
    context = {
        "form": TransactionForm(instance=transaction),
        "transaction": transaction,
    }

    # Render the transaction_update.html template
    return render(request, "tracker/partials/transaction_update.html", context)


# Transaction delete view
@login_required
@require_http_methods(["DELETE"])
def transaction_delete(request, pk):
    """Transaction delete view

    Args:
        request (HttpRequest): The request object
        pk (int): The primary key of the transaction

    Returns:
        HttpResponse: The response object
    """

    # Get the transaction object for the authenticated user
    transaction = get_object_or_404(Transaction, pk=pk, user=request.user)

    # Delete the transaction
    transaction.delete()

    # Create a context dictionary
    context = {
        "message": f"Transaction Amount: {transaction.amount} Date: {transaction.date} deleted successfully!"
    }

    # Render the transaction_success.html template
    return render(request, "tracker/partials/transaction_success.html", context)


# Transactions get view
@login_required
def transactions_get(request):
    """Transactions get view

    Args:
        request (HttpRequest): The request object

    Returns:
        JsonResponse: The response object
    """

    # Get the page number from the request
    page = request.GET.get("page", 1)

    # Create a transaction filter
    transaction_filter = TransactionFilter(
        data=request.GET,
        queryset=Transaction.objects.filter(user=request.user).select_related(
            "category"
        ),
    )

    # Paginate the transactions
    paginator = Paginator(transaction_filter.qs, settings.PAGE_SIZE)

    # Get the page from the paginator
    transaction_page = paginator.get_page(page)

    # Create a context dictionary
    context = {
        "transactions": transaction_page,
    }

    # Render the transactions_container.html template
    return render(
        request,
        "tracker/partials/transactions_container.html#transaction_list",
        context,
    )


# Transaction charts view
@login_required
def transactions_charts(request):
    """Transaction charts view

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

    # Plot the income expense bar chart
    income_expense_bar_chart = plot_income_expense_bar_chart(transaction_filter.qs)

    # Plot the category pie chart
    category_income_pie_chart = plot_category_pie_chart(
        transaction_filter.qs.filter(type="INCOME"),
        title="Income by Category",
    )
    category_expense_pie_chart = plot_category_pie_chart(
        transaction_filter.qs.filter(type="EXPENSE"),
        title="Expense by Category",
    )

    # Create a context dictionary
    context = {
        "filter": transaction_filter,
        "income_expense_bar_chart": income_expense_bar_chart.to_html(),
        "category_income_pie_chart": category_income_pie_chart.to_html(),
        "category_expense_pie_chart": category_expense_pie_chart.to_html(),
    }

    # If the request is htmx request
    if request.htmx:
        # Render the charts_container.html template
        return render(request, "tracker/partials/charts_container.html", context)

    # Render the transactions_charts.html template
    return render(request, "tracker/transactions_charts.html", context)


# Transaction export view
@login_required
def transactions_export(request):
    """Transaction export view

    Args:
        request (HttpRequest): The request object

    Returns:
        HttpResponse: The response object
    """

    # If the request is htmx request
    if request.htmx:
        # Send a redirect response
        return HttpResponse(headers={"HX-Redirect": request.get_full_path()})

    # Create a transaction filter
    transaction_filter = TransactionFilter(
        data=request.GET,
        queryset=Transaction.objects.filter(user=request.user).select_related(
            "category"
        ),
    )

    # Export the queryset to dataset
    dataset = TransactionResource().export(transaction_filter.qs)

    # Create a response object
    response = HttpResponse(
        dataset.csv,
        content_type="text/csv",
    )
    response["Content-Disposition"] = 'attachment; filename="transactions.csv"'

    # Return the response object
    return response


# Transactions import view
@login_required
def transactions_import(request):
    """Transaction import view

    Args:
        request (HttpRequest): The request object

    Returns:
        HttpResponse: The response object
    """

    # If the request is POST
    if request.method == "POST":
        # Get the file from the request
        file = request.FILES.get("file")

        # Create a dataset from the file
        dataset = Dataset().load(file.read().decode("utf-8"), format="csv")

        # Initialize the result
        result = TransactionResource().import_data(
            dataset, user=request.user, dry_run=True
        )

        # If the result has no errors
        if not result.has_errors():
            # Import the data
            result = TransactionResource().import_data(
                dataset, user=request.user, dry_run=False
            )

            # Create a context dictionary
            context = {
                "message": f"{result.total_rows} transactions imported successfully!"
            }

            # Render the transaction_success.html template
            return render(request, "tracker/partials/transaction_success.html", context)

        # If the result has errors
        else:
            # Create a context dictionary
            context = {"message": "Sorry, An Error Occurred while Importing the Data!"}

            # Render the transaction_errors.html template
            return render(request, "tracker/partials/transaction_errors.html", context)

    # Create a context dictionary
    context = {}

    # Render the transactions_import.html template
    return render(request, "tracker/partials/transactions_import.html", context)
