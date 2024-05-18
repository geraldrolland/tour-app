from django.contrib import admin
from .models import City, TouristPurchase

admin.site.register([City, TouristPurchase])
