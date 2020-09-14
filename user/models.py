from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
# Create your models here.


class User(AbstractUser):
    phone_number = models.CharField(default='', max_length=10, blank=True)
    address = models.CharField(default='', max_length=255, blank=True)
    dob = models.DateTimeField(default=timezone.datetime.now())
    passport = models.CharField(default='', max_length=15, blank=True)

