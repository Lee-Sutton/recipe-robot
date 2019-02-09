from recipes.models import Recipe, Ingredient
import factory


class RecipeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Recipe

    name = 'dummy recipe'
    description = 'dummy description'


class IngredientFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ingredient

    name = 'dummy ingredient'
    amount = 0.5
