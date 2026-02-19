from django.db import models

class MyUser(models.Model):
    nickname = models.TextField()
    username = models.TextField()
    password = models.TextField()

    datebirth = models.DateField()
    interests = models.JSONField()
    
    
