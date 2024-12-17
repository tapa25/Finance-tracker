# Imports
from django.shortcuts import render


# Index view
def index(request):
    # Render the index.html template
    return render(request, "tracker/index.html")
