# Imports
from django.contrib import admin

from apps.tracker.models import Category, Transaction

# Register the models
admin.site.register(Category)
admin.site.register(Transaction)
