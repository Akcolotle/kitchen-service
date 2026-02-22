from django import forms
from kitchen.models import Dish
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = "__all__"


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1", "password2")