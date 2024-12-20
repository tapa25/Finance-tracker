# Imports
from django import forms

from apps.tracker.models import Category, Transaction


# Transaction form
class TransactionForm(forms.ModelForm):
    """Transaction form

    Inherits:
        forms.ModelForm

    Fields:
        category (forms.ModelChoiceField): The category field

    Methods:
        clean_amount: Method to clean the amount field

    Meta:
        model (Transaction): The Transaction model
        fields (tuple): The fields to include in the form
        widgets (dict): The widgets for the fields
    """

    # Fields
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={"class": "form-select"}),
    )

    # Method to clean the amount field
    def clean_amount(self):
        """Method to clean the amount field

        Returns:
            float: The cleaned amount
        """

        # Attributes
        amount = self.cleaned_data["amount"]

        # Check if the amount is less than or equal to 0
        if amount <= 0:
            # Raise a validation error
            raise forms.ValidationError("Amount must be greater than 0")

        # Return the cleaned amount
        return amount

    # Meta
    class Meta:
        # Attributes
        model = Transaction
        fields = (
            "type",
            "amount",
            "date",
            "category",
        )
        widgets = {"date": forms.DateInput(attrs={"type": "date"})}
