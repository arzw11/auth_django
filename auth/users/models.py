from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    date_birth = models.DateField(blank=True, null=True, verbose_name='Дата рождения')



