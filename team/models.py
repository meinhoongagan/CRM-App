from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Team(models.Model):
    name =models.CharField( max_length=50)
    member=models.ManyToManyField(User, related_name='teams')
    created_by=models.ForeignKey(User, related_name="created_teams",on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    