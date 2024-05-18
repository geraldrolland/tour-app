from django.db import models
from accounts.models import CustomUser
import uuid
from datetime import datetime


class City(models.Model):
    name=models.CharField(max_length=64, null=False)
    city_id = models.CharField(max_length=64, auto_created=str(uuid.uuid4), primary_key=True)
    description = models.TextField(null=False, blank=False)
    city_poster = models.ImageField(upload_to="static/images/")
    tourist_price = models.IntegerField(null=False, blank=False)
    upload_date = models.DateField(auto_now_add=datetime.now)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


class TouristPurchase(models.Model):
    city_id = models.ForeignKey(City, on_delete=models.CASCADE)
    purchase_id = models.CharField(max_length=36, null=False, blank=False, auto_created=str(uuid.uuid3))
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    payment_status = models.BooleanField(default=False)
    purchase_date = models.DateField(auto_now_add=datetime.now())


