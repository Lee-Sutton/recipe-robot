"""recipes models test suite"""
from django.test import TestCase
from recipes.models import Recipes


class TestRecipes(TestCase):
    """Test suite for recipes model"""
    def test_inserting_into_db(self):
        """it should insert into the database"""
        recipe = Recipes(name='test', amount=1)
        recipe.save()
        assert Recipes.objects.filter(name='test').count() == 1
