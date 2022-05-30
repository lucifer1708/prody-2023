from django.db import models

# Create your models here.


class EventCard(models.Model):
    title = models.CharField(max_length=30)
    poster = models.ImageField(
        upload_to='poster/', blank=False, null=False)
    desc = models.TextField()

    def __str__(self):
        return "{} - {}".format(self.title, self.desc)
