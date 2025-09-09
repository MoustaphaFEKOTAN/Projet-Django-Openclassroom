from django.contrib import admin

# Register your models here.
from listings.models import Band,Listing

admin.site.register(Band)
admin.site.register(Listing)