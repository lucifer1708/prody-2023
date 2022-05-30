from django.db import models
from django.conf import settings
# Create your models here.


class ExtendedUser(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    phone_number = models.IntegerField(blank=True)
