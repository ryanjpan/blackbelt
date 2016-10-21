from __future__ import unicode_literals

from django.db import models

from ..login.models import User

class Product(models.Model):
    users = models.ManyToManyField(User)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    adder = models.ForeignKey(User, on_delete=models.CASCADE, related_name='madeproduct')
