from django.test import TestCase
from recipes.models import Recipe, Ingredient
from recipes.factories import RecipeFactory, IngredientFactory


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


class TestIngredientFactory(TestCase):
    def setUp(self):
        IngredientFactory()
        self.ingredients = Ingredient.objects.all()

    def test_factory_create(self):
        """It should insert a recipe into the database"""
        assert len(self.ingredients)

    def test_properties_are_valid(self):
        ingredient = self.ingredients[0]
        assert isinstance(ingredient.name, str)
        assert isinstance(ingredient.amount, float)

