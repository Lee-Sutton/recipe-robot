"""
Recipe App Models
=================

- This module defines the models used the recipes app.
- Corresponding tests can be found in test_models.py
"""
from django.db import models


class Recipe(models.Model):
    """Recipe model"""
    name = models.CharField(max_length=255)
    description = models.TextField()


class Ingredient(models.Model):
    """Ingredients model"""
    name = models.CharField(max_length=255)
    amount = models.FloatField()
