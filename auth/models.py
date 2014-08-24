from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    desc = models.URLField(max_length=4000)
    year = models.IntegerField(default=2012)