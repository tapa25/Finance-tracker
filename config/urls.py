# Imports
from django.conf import settings
from django.contrib import admin
from django.urls import path

# Set the django urls
urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
]

# Admin configuration
admin.site.site_header = "Finance Tracker Admin"
admin.site.site_title = "Finance Tracker Admin"
admin.site.index_title = "Welcome to Finance Tracker Admin"
