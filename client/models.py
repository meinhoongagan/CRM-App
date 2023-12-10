from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    description = models.TextField()
    created_by = models.ForeignKey(User, related_name='client', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
# models.py
from django.db import models

class Activity(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    # Other fields relevant to the activity

