from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User

# class CustomUser(AbstractUser):
#     pass

class Lead(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    message = models.CharField(max_length=500, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, related_name="leads", on_delete=models.CASCADE, null=True)
