# Imports
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


# TrackerConfig
class TrackerConfig(AppConfig):
    """TrackerConfig

    Inherits:
        AppConfig

    Attributes:
        default_auto_field (str): "django.db.models.BigAutoField"
        name (str): "tracker"
        verbose_name (str): _("Tracker")
    """

    # Attributes
    default_auto_field = "django.db.models.BigAutoField"
    name = "tracker"
    verbose_name = _("Tracker")
