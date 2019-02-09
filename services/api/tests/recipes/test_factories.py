from django.test import TestCase
from recipes.models import Recipe, Ingredient
from recipes.factories import RecipeFactory


class TestRecipeFactory(TestCase):
    """Recipe factory test suite"""

    def setUp(self):
        RecipeFactory()
        self.recipes = Recipe.objects.all()

    def test_factory_create(self):
        """It should insert a recipe into the database"""
        assert len(self.recipes)

    def test_properties_are_valid(self):
        recipe = self.recipes[0]
        assert isinstance(recipe.name, str)
        assert isinstance(recipe.description, str)
