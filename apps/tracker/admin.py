# Imports
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from apps.tracker.models import Category, Transaction

# Get the User model
User = get_user_model()


# Register the User model
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """User model admin view

    Attributes:
        list_display (tuple): The fields to display in the list.
        list_display_links (tuple): The fields to link in the list.
        search_fields (tuple): The fields to search in the list.
        ordering (tuple): The default ordering for the list.
        fieldsets (tuple): The fieldsets to display in the form.
        add_fieldsets (tuple): The fieldsets to display in the add form.
    """

    # Attributes
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "is_active",
        "is_superuser",
    )
    list_display_links = ("email", "username")
    search_fields = ("email", "first_name", "last_name")
    ordering = ("-date_joined",)
    fieldsets = (
        (_("Login Credentials"), {"fields": ("email", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "username")}),
        (
            _("Permissions and Groups"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (_("Important Dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "email",
                    "first_name",
                    "last_name",
                    "password1",
                    "password2",
                ),
            },
        ),
    )


# Register the Category model
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Category model admin view

    Attributes:
        list_display: Fields to display in the admin view
        search_fields: Fields to search in the admin
    """

    # Attributes
    list_display = ("name",)
    search_fields = ("name",)


# Register Transaction model
@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    """Transaction model admin view

    Attributes:
        list_display: Fields to display in the admin view
        list_display_links: Fields to display as links in the admin view
        list_filter: Fields to filter in the admin view
        search_fields: Fields to search in the admin
        ordering: Fields to order in the admin view
        autocomplete_fields: Fields to autocomplete in the admin view
    """

    # Attributes
    list_display = ("date", "user", "category", "type", "amount")
    list_display_links = ("date", "user", "category", "type", "amount")
    list_filter = ("date", "user", "category", "type")
    search_fields = ("date", "user__username", "category__name", "type", "amount")
    ordering = ("-date", "user", "category", "type", "amount")
    autocomplete_fields = ("user", "category")
