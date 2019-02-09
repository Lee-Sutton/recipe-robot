from recipes.models import Recipe, Ingredient
import factory


class RecipeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Recipe

    name = 'dummy recipe'
    description = 'dummy description'
