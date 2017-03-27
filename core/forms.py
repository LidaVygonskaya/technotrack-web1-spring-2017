from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from application import settings
from core.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2')