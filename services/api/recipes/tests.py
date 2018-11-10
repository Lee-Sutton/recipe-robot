from django.test import TestCase
from .models import Recipes


class TestRecipes(TestCase):
    """Test suite for recipes model"""
    def test_inserting_into_db(self):
        """it should insert into the database"""
        recipe = Recipes(name='test', amount=1)
        recipe.save()
        self.assertGreater(Recipes.objects.filter(name='test').count(), 0)
