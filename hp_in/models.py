from django.db import models

class Information(models.Model):
    Country_name = models.CharField(max_length=100)
    Ladder_score = models.DecimalField(max_digits=6, decimal_places=3)
    Logged_GDP_per_capita = models.DecimalField(max_digits=6, decimal_places=3)
    Healthy_life_expectancy = models.DecimalField(max_digits=6, decimal_places=3)
    Generosity = models.DecimalField(max_digits=6, decimal_places=3)