from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from application import settings
from core.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('first_name','last_name','email','username', 'password1', 'password2','avatar')