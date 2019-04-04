from django.urls import path

# Import views to link to the urls
from . import views

urlpatterns = [
    # below path is like /listings
    path('', views.index, name='listings'),

    # /listings/23
    path('<int:listing_id>', views.listing, name='listing'),

    # listings/search
    path('search', views.search, name='search'),

    # views.index is the method name, and name='index' is to easily
    # use index name
]
