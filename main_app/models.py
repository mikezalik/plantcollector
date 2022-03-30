from django.db import models
from django.urls import reverse

CARE = (
    ('W', 'Water'),
    ('F', 'Fertilizer'),
)

class Plant(models.Model):
        name = models.CharField(max_length=100)
        species = models.CharField(max_length=100)
        description = models.TextField(max_length=250)

def __str__(self):
    return f"Plant named {self.name}"

def get_absolute_url(self):
    return reverse('detail', kwargs={'plant_id': self.id})

class Care(models.Model):
    date = models.DateField('Care Date')
    care = models.CharField(
        max_length=1,
        choices = CARE,
        default = CARE[0][0],
    )

plant = models.ForeignKey(
    Plant, 
    on_delete=models.CASCADE
)

def __str__(self):
    return f"{self.get_care_display()} on {self.date}"

class Meta:
    ordering=['-date']