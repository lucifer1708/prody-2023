from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class EventCard(models.Model):
    title = models.CharField(max_length=30)
    poster = models.ImageField(
        upload_to='poster/', blank=False, null=False)
    desc = models.TextField()
    slug = models.SlugField(blank=True)

    def __str__(self):
        return "{} - {}".format(self.title, self.desc)


class Sponsors(models.Model):
    image = models.ImageField(upload_to='sponsors/', blank=False, null=False)
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=30)

    def __str__(self):
        return "{} - {}".format(self.title, self.subtitle)


class AddEvent(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    event = models.ForeignKey(EventCard, null=True, on_delete=models.CASCADE)
    event_title = models.CharField(null=True, max_length=20)
    name = models.CharField(null=True, max_length=20)
    email = models.EmailField(null=True)

    def placeOrder(self):
        self.save()

    def __str__(self):
        return "{} - {}".format(self.event_title, self.name, self.email)
