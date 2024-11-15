from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    USER = 'user'
    ADMIN = 'admin'
    MANAGER = 'manager'
    MERCHANT = 'merchant'
    
    ROLE_CHOICES = [
        (USER, 'User'),
        (ADMIN, 'Admin'),
        (MANAGER, 'Manager'),
        (MERCHANT, 'Merchant'),
    ]
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default=USER)
    # ...existing code...
