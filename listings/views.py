from django.shortcuts import render
from .models import Listing
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime
# Create your views here.


def index(request):
    listings_query = request.GET.get('q')
    # listings = None
    if listings_query:
        listings = Listing.objects.filter(title__icontains=listings_query).filter(is_published=True)
    else:
        listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    # else:
    # All the rows in the listings model
    count = str(len(listings))
    current_year = datetime.now().year
    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {'listings_active': 'active',
               'listings': paged_listings,
               'total_listings': count,
               'current_year': current_year
               }
    return render(request, 'listings/listings.html', context=context)


def listing(request, listing_id):
    return render(request, 'listings/listing.html')


def search(request):
    return render(request, 'listings/search.html')


