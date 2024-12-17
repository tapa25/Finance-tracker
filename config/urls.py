# Imports
from django.conf import settings
from django.contrib import admin
from django.urls import path

# Django admin urls
urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
]

# If DEBUG is True
if settings.DEBUG:
    # Import static
    from django.conf.urls.static import static

    # Add static and media urls
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Admin configuration
admin.site.site_header = "Finance Tracker Admin"
admin.site.site_title = "Finance Tracker Admin"
admin.site.index_title = "Welcome to Finance Tracker Admin"
