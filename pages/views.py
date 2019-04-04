from django.shortcuts import render
from datetime import datetime

# Create your views here.


def index(request):
    current_year = datetime.now().year
    context = {
        'current_year': current_year
    }
    return render(request, "pages/index.html", context)


def about(request):
    return render(request, "pages/about.html")

