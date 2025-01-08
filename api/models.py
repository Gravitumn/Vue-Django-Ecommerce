from django.db import models

from django.db import models
from django.forms import ValidationError
from django.core.validators import MinValueValidator
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    ADMIN = 'admin'
    DEVELOPER = 'developer'
    USER = 'user'

    ROLE_CHOICES = [
        (ADMIN, 'Admin'),
        (DEVELOPER, 'Developer'),
        (USER, 'User'),
    ]

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default=USER)

    def __str__(self):
        return self.username
    

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2,validators=[MinValueValidator(0)]) 
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  

    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)  
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  
    amount = models.IntegerField()

    def clean(self):
        if self.amount < 0:
            raise ValidationError("Amount cannot be negative")

class Cart(models.Model):  
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField(validators=[MinValueValidator(0)])

    class Meta:
        unique_together = ('user', 'product')  
