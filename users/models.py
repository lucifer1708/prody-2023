from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.templatetags.static import static
from django.contrib.auth.models import AbstractUser


class ExtendedUser(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(max_length=13, blank=True)


class Profile(models.Model):
    GENDER_MALE = 1
    GENDER_FEMALE = 2
    GENDER_OTHER = 3
    GENDER_CHOICES = [
        (GENDER_MALE, _("Male")),
        (GENDER_FEMALE, _("Female")),
        (GENDER_OTHER, _("Other")),
    ]

    user = models.OneToOneField(
        User, related_name="profile", on_delete=models.CASCADE)
    avatar = models.ImageField(
        upload_to="participants/profiles/avatars/", null=True, blank=True)
    birthday = models.CharField(null=True, max_length=12, blank=True)
    gender = models.PositiveSmallIntegerField(
        choices=GENDER_CHOICES, null=True, blank=True)
    phone_number = models.CharField(null=True, max_length=13, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')

    @ property
    def get_avatar(self):
        return self.avatar.url if self.avatar else static('images/avatars/default-profile-picture.png')
