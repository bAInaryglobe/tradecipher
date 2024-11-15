from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

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
    date_of_birth = models.DateField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def is_admin(self):
        return self.role == self.ADMIN
    
    def is_manager(self):
        return self.role == self.MANAGER
    
    def is_merchant(self):
        return self.role == self.MERCHANT
    
    def __str__(self):
        return self.username
    # ...existing code...
