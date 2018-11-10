from django.db import models


class Recipes(models.Model):
    """Recipes model"""
    name = models.CharField(max_length=255)
    amount = models.FloatField()
