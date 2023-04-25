from django.db import models
from django.urls import reverse

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length = 150)
    classifier = models.CharField(max_length = 150)
    description = models.TextField(max_length = 300)
    number = models.IntegerField()

    def __str__(self):
        return f"{self.name} is a {self.classifier}."
    
class Event(models.Model):
    name = models.CharField(max_length = 150)
    type = models.CharField(max_length = 150)
    description = models.TextField(max_length = 300)
    rating = models.IntegerField()

    def __str__(self):
        return f"{self.name} is a {self.type} event."

    def get_absolute_url(self):
        return reverse('detail', kwargs={'event_id': self.id})