# need from django to support ORM i believe?
from django.db import models

# define class
class Appointment(models.Model):
    """Database model for tracking walker appointments"""
    completed = models.BooleanField(default=False)
    date = models.DateField()
    walker = models.ForeignKey('Walker', on_delete=models.CASCADE, related_name='appointments')


