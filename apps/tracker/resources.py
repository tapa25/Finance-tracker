# Imports
from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget

from apps.tracker.models import Category, Transaction


# TransactionResource class
class TransactionResource(resources.ModelResource):
    """TransactionResource class

    Inherits:
        resources.ModelResource

    Fields:
        category (Field): Category field

    Meta:
        model (Model): Transaction model
        fields (tuple): Fields to include in the resource
    """

    # Fields
    category = fields.Field(
        column_name="category",
        attribute="category",
        widget=ForeignKeyWidget(Category, field="name"),
    )

    # Meta
    class Meta:
        # Attributes
        model = Transaction
        fields = ("date", "category", "type", "amount")
