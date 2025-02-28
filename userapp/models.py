from django.db import models
from django.contrib.auth.hashers import make_password

class Token(models.Model):
    id = models.AutoField(primary_key=True)
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    expires_at = models.DateTimeField()
    user_id = models.IntegerField()
    is_used = models.BooleanField(default=False)

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=225)
    phone = models.CharField(max_length=10, null=True, blank=True)
    country = models.CharField(max_length=100, default="Unknown", blank=True, null=True)

    def __str__(self) -> str:
        return self.name
