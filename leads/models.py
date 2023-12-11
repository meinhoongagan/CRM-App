from django.db import models
from django.contrib.auth.models import User
from team.models import Team
# Create your models here.
class Lead(models.Model):
    team=models.ForeignKey(Team, related_name="leads", on_delete=models.CASCADE)
    name=models.CharField( max_length=50)
    id = models.AutoField(primary_key=True)
    email=models.EmailField( max_length=254)
    description=models.TextField()
    NEW='New'
    CONTACED='Contacted'
    WON="Won"
    LOSE='Lose'
    CHOICES_STATUS=(
        (NEW,'New'),
        (CONTACED,'Contacted'),
        (WON,'Won'),
        (LOSE,'Lose'),
    )
    status=models.CharField(choices=CHOICES_STATUS, max_length=50,default="New")
    LOW='Low'
    MEDIUM='Medium'
    HIGH='High'
    CHOICES_PRIORTY=(
        (LOW,'Low'),
        (MEDIUM,'Medium'),
        (HIGH,'High'),
    )
    priority=models.CharField(choices=CHOICES_PRIORTY, max_length=50,default=MEDIUM)
    created_by=models.ForeignKey(User, related_name='leads', on_delete=models.CASCADE)
    converted_to_client=models.BooleanField(default=False)
    created_at=models.DateTimeField(  auto_now_add=True)
    modified_at=models.DateTimeField( auto_now=True)
    class Meta:
        ordering=("name",)
    def __str__(self):
        return self.name
    