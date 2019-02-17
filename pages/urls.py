from django.urls import path

# Import views to link to the urls
from . import views

urlpatterns = [
    path('', views.index, name='index')
    # views.index is the method name, and name='index' is to easily
    # use index name
]