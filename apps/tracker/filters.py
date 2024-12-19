# Imports
import django_filters
from django import forms

from apps.tracker.models import Category, Transaction


# Transaction Filter
class TransactionFilter(django_filters.FilterSet):
    """Transaction Filter

    Inherits:
        django_filters.FilterSet

    Attributes:
        transaction_type (django_filters.ChoiceFilter): Transaction Type Filter

    Meta:
        model: Transaction
        fields: ("transaction_type",)
    """

    # Attributes
    transaction_type = django_filters.ChoiceFilter(
        field_name="type",
        choices=Transaction.TRANSACTION_TYPE_CHOICES,
        label="Transaction Type",
        lookup_expr="iexact",
        empty_label="Any",
    )
    start_date = django_filters.DateFilter(
        field_name="date",
        lookup_expr="gte",
        label="Date From",
        widget=forms.DateInput(attrs={"type": "date"}),
    )
    end_date = django_filters.DateFilter(
        field_name="date",
        lookup_expr="lte",
        label="Date To",
        widget=forms.DateInput(attrs={"type": "date"}),
    )
    category = django_filters.ModelMultipleChoiceFilter(
        field_name="category",
        queryset=Category.objects.all(),
        label="Category",
        widget=forms.SelectMultiple(),
    )

    # Meta
    class Meta:
        # Attributes
        model = Transaction
        fields = ("transaction_type", "start_date", "end_date", "category")
