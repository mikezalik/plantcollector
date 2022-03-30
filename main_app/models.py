from smtplib import SMTPRecipientsRefused
from django.db import models

# Create your models here.

class Plant:
    def __init__(self, name, species, description):
        self.name: name
        self.species: species
        self.description: description

plants = [
    Plant('Snake Plant', 'Dracaena Trifasciata', 'Slender, vertical, dark green leaves bordered by light green'),
    Plant('Swiss Cheese Plant', 'Monstera', 'Large leafy greens with holes in them')

]