"""
Recipe App Models
=================

- This module defines the models used the recipes app.
- Corresponding tests can be found in test_models.py
"""
from django.db import models


class Recipes(models.Model):
    """Recipes model"""
    name = models.CharField(max_length=255)
    amount = models.FloatField()
