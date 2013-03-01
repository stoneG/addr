from django.db import models
from django.contrib.auth.models import User

class Addresses(models.Model):
    name = models.CharField(max_length=100)
    line_one = models.CharField(max_length=100)
    line_two = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=5)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.name
