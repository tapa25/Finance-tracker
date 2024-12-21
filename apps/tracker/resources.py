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
        import_id_fields (tuple): Fields to use as unique identifiers
    """

    # Fields
    category = fields.Field(
        column_name="category",
        attribute="category",
        widget=ForeignKeyWidget(Category, field="name"),
    )

    # Function to run after object initialization
    def after_init_instance(self, instance, new, row, **kwargs) -> None:
        """Function to run after object initialization

        Args:
            instance (Model): Model instance
            new (bool): Whether the instance is new
            row (dict): Row data
            **kwargs: Keyword arguments
        """
        # Set the user
        instance.user = kwargs.get("user")

    # Meta
    class Meta:
        # Attributes
        model = Transaction
        fields = ("date", "category", "type", "amount")
        import_id_fields = ("date", "category", "type", "amount")
