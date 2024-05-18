from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import CustomUser
class CustomUserCreationForm(UserCreationForm):
    class meta:
        models = CustomUser
        fields = ("email",)

class CustomUserChangeForm(UserChangeForm):
    class meta:
        model = CustomUser
        fields = ("email",)

