# Imports
from django.urls import path

from apps.tracker import views as tracker_views

# Set the app name
app_name = "tracker"

# URL patterns
urlpatterns = [
    path("", tracker_views.index, name="index"),
    path("transactions/", tracker_views.transactions_list, name="transactions_list"),
]
