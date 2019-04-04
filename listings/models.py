from django.db import models
from datetime import datetime
from realtors.models import Realtor

class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    garage = models.IntegerField(default=0)
    # Bathrooms can be shared and thus are called as 1.5 etc
    # Thus I will keep it Decimal Field
    # https://community.withairbnb.com/t5/Help/Shared-bathroom-classification-1-5-or-ZERO/td-p/280614
    bathrooms = models.DecimalField(decimal_places=1, max_digits=2)
    sqft = models.IntegerField()
    #For lot size:- Eg. 3.5 Acres etc.
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    # Better set MEDIA folder now
    # Photos should go in a format like that as date
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now(), blank=True)
#     To show field in admin area
    def __str__(self):
        return self.title


