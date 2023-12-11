from django.db import models
from django.contrib.auth.models import User
from team.models import Team
class Client(models.Model):
    team=models.ForeignKey(Team,related_name="clients", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    description = models.TextField()
    created_by = models.ForeignKey(User, related_name='client', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering=("name",)
    def __str__(self):
        return self.name
# models.py
from django.db import models

class Activity(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    # Other fields relevant to the activity