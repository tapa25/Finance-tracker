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
