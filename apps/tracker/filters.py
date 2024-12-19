# Imports
import django_filters

from apps.tracker.models import Transaction


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

    # Meta
    class Meta:
        # Attributes
        model = Transaction
        fields = ("transaction_type",)
