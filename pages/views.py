from django.shortcuts import render
from datetime import datetime
from listings.models import Listing
from realtors.models import Realtor
from choices import bedroom_choices, price_choices, states

# Highlights: Create your views here.


def index(request):
    listings = Listing.objects.order_by("-list_date").filter(is_published=True)[:3]
    current_year = datetime.now().year
    context = {
        "current_year": current_year,
        "listings": listings,
        "bedrooms": bedroom_choices,
        "prices": price_choices,
        "states": states,
    }

    return render(request, "pages/index.html", context)


def about(request):
    realtors = Realtor.objects.order_by("-hire_date")
    top_realtor = Realtor.objects.all().filter(is_mvp=True)
    if len(top_realtor) < 0:
        top_realtor = ""
    else:
        top_realtor = top_realtor[0]
    context = {"top_realtor": top_realtor, "realtors": realtors[0:3]}
    return render(request, "pages/about.html", context=context)

