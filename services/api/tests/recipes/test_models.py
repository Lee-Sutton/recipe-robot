"""recipes models test suite"""
from django.test import TestCase
from recipes.models import Recipe, Ingredient


class TestRecipe(TestCase):
    """Test suite for recipes model"""

    def test_inserting_into_db(self):
        """it should insert into the database"""
        recipe = Recipe(name='test', description='This is a recipe')
        recipe.save()
        assert Recipe.objects.filter(name='test').count() == 1


class TestIngredient(TestCase):
    """Test suite for ingredients model"""

    def test_inserting_into_db(self):
        """it should insert into the database"""
        ingredient = Ingredient(name='test', amount=1)
        ingredient.save()
        assert Ingredient.objects.filter(name='test').count() == 1
