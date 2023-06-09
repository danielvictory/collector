from django.db import models
from django.urls import reverse

from datetime import date
from django.contrib.auth.models import User

# Variables for use in models
times_of_day = (
    ('M', 'Morning'),
    ('A', 'Afternoon'),
    ('E', 'Evening'),
    ('N', 'Night')
)

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length = 150)
    classifier = models.CharField(max_length = 150)
    description = models.TextField(max_length = 300)
    number = models.IntegerField()

    def __str__(self):
        return f"{self.name} is a {self.classifier}."

class Performer(models.Model):
    name = models.CharField(max_length = 150)
    profession = models.CharField(max_length = 150)

    def __str__(self):
        return f'{self.name} is a {self.profession}.'

    def get_absolute_url(self):
        return reverse('performer_detail', kwargs={'pk': self.id})
    
class Event(models.Model):
    name = models.CharField(max_length = 150)
    type = models.CharField(max_length = 150)
    description = models.TextField(max_length = 300)
    rating = models.IntegerField()

    performers = models.ManyToManyField(Performer)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} is a {self.type} event."

    def get_absolute_url(self):
        return reverse('detail', kwargs={'event_id': self.id})

class Schedule(models.Model):
    date = models.DateField('Schedule Date')
    timeofday = models.CharField(
        max_length = 1,
        choices=times_of_day,
        default=times_of_day[2][0])

    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return f"Scheduled for the {self.get_timeofday_display()} on {self.date}"

    class Meta:
        ordering = ['-date']