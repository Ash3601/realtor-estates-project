from django.contrib import admin
from .models import Realtor


class RealtorAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone']
    list_display_links = ['name']
    search_fields = ('name', 'email')


admin.site.register(Realtor, RealtorAdmin)
