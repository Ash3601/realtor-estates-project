from django.urls import path

# Import views to link to the urls
from . import views

urlpatterns = [
    # below path is like /listings
    path('contact', views.contact, name='contact'),
]
