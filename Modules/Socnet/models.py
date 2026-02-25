from django.db import models
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    datebirth = models.DateField(null=True)
    interests = models.JSONField(null=True)
    
    

