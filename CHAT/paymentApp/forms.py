from django import forms
from .models import City
class ImageForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ["name", "description", "city_poster", "tourist_price"]