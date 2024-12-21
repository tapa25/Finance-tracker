# Imports
import plotly.graph_objects as go
from django.db.models import Sum
from django.db.models.query import QuerySet


# Function to plot a bar chart
def plot_income_expense_bar_chart(queryset: QuerySet) -> go.Figure:
    """Plot an income vs expense bar chart

    Args:
        queryset (QuerySet): The queryset of transactions

    Returns:
        go.Figure: The bar chart figure
    """

    # Get the income transactions
    income_transactions = queryset.filter(type="INCOME")

    # Get the expense transactions
    expense_transactions = queryset.filter(type="EXPENSE")

    # Create the bar chart
    fig = go.Figure(
        data=[
            go.Bar(
                name="Income",
                x=["Income"],
                y=[income_transactions.aggregate(total=Sum("amount"))["total"]],
            ),
            go.Bar(
                name="Expense",
                x=["Expense"],
                y=[expense_transactions.aggregate(total=Sum("amount"))["total"]],
            ),
        ]
    )

    # Update the layout
    fig.update_layout(
        title="Income vs Expense",
        xaxis_title="Transaction Type",
        yaxis_title="Amount",
        barmode="group",
    )

    # Return the figure
    return fig


# Function to plot a category pie chart
def plot_category_pie_chart(queryset: QuerySet, title: str) -> go.Figure:
    """Plot a category pie chart

    Args:
        queryset (QuerySet): The queryset of transactions
        title (str): The title of the pie chart

    Returns:
        go.Figure: The pie chart figure
    """

    # Get the category amounts
    category_amounts = queryset.values("category__name").annotate(total=Sum("amount"))

    # Create the pie chart
    fig = go.Figure(
        data=[
            go.Pie(
                labels=[category["category__name"] for category in category_amounts],
                values=[category["total"] for category in category_amounts],
            )
        ]
    )

    # Update the layout
    fig.update_layout(title=title)

    # Return the figure
    return fig
