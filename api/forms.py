from django import forms
from django.contrib.auth.models import User as Usermodel
from .models import Product
from django.contrib.auth import get_user_model

User = get_user_model()


class CreateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email', 'password']

    def save(self, commit=True) -> Usermodel:
        user = super().save(commit=False)
        user.username = self.cleaned_data["username"]
        user.email = self.cleaned_data["email"]
        user.set_password(self.cleaned_data["password"])
        user.role = User.USER
        if commit:
            user.save()
        return user

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'image','user']
