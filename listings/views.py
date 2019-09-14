from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime
from listings.models import Listing
from django.shortcuts import get_object_or_404
from choices import bedroom_choices, price_choices, states

# Create your views here.


def index(request):
    listings_query = request.GET.get("q")
    # listings = None
    if listings_query:
        listings = Listing.objects.filter(title__icontains=listings_query).filter(
            is_published=True
        )
    else:
        listings = Listing.objects.order_by("-list_date").filter(is_published=True)

    # else:
    # All the rows in the listings model
    count = str(len(listings))
    current_year = datetime.now().year
    paginator = Paginator(listings, 6)
    page = request.GET.get("page")
    paged_listings = paginator.get_page(page)

    context = {
        "listings_active": "active",
        "listings": paged_listings,
        "total_listings": count,
        "current_year": current_year,
    }
    return render(request, "listings/listings.html", context=context)


def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {"listing": listing}
    return render(request, "listings/listing.html", context)


def search(request):
    queryset_list = Listing.objects.order_by("-list_date")

    # ? Keywords
    if "keywords" in request.GET:
        keywords = request.GET["keywords"]
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    # ? City
    if "city" in request.GET:
        city = request.GET["city"]
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    # ? State
    if "state" in request.GET:
        state = request.GET["state"]
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)
            print(queryset_list.filter(state__iexact=state))

    # ? Bedrooms
    if "bedrooms" in request.GET:
        bedrooms = request.GET["bedrooms"]
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)
            print(queryset_list.filter(bedrooms__lte=bedrooms))

    # ? Price
    if "price" in request.GET:
        price = request.GET["price"]
        if price:
            queryset_list = queryset_list.filter(price__lte=price)
            print(queryset_list.filter(price__lte=price))

    context = {
        "bedrooms": bedroom_choices,
        "prices": price_choices,
        "listings": queryset_list,
        "states": states,
        "values": request.GET,
    }

    return render(request, "listings/search.html", context)

