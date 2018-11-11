from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Recipe, Ingredient
from .serializers import IngredientSerializer, RecipeSerializer


class ListRecipe(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = (permissions.IsAuthenticated, )


class DetailRecipe(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = (permissions.IsAuthenticated, )
