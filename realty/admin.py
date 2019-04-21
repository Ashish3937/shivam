from django.contrib import admin
from django.db import models
from .models import Booking, Contact, PropertyType, Listing
# Register your models here.
admin.site.register(Booking)
admin.site.register(Contact)
admin.site.register(PropertyType)
admin.site.register(Listing)