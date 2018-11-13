"""
Serializes the recipes models for transport over the api layer
for more info see:
https://www.django-rest-framework.org/api-guide/serializers/
"""
from rest_framework import serializers
from .models import Ingredient, Recipe


class RecipeSerializer(serializers.ModelSerializer):
    """serializer for the recipe model"""
    class Meta:
        fields = ('id', 'name', 'description')
        model = Recipe


class IngredientSerializer(serializers.ModelSerializer):
    """serializer for the ingredient model"""
    class Meta:
        fields = ('id', 'name', 'amount')
        model = Ingredient
