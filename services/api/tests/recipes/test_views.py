"""recipes views test suite"""
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from recipes.factories import IngredientFactory, RecipeFactory
from recipes.models import Ingredient, Recipe


def create_user(username='test_user', email='test_user@e.com',
                password='secret'):
    """Creates a user for testing purposes"""
    user = User(username=username, email=email)
    user.set_password(password)
    user.save()
    return user


class TestRecipeViews(APITestCase):
    """Recipe rest endpoints"""

    def test_recipe_list(self):
        """it should return a list of recipes in the database"""
        user = create_user()
        self.client.force_authenticate(user)
        response = self.client.get('/api/v1/', format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data is not None

    def test_recipe_list_is_protected(self):
        """it should require the user to be authenticated to the
        view the resources
        """
        response = self.client.get('/api/v1/', format='json')
        assert response.status_code == status.HTTP_403_FORBIDDEN


class TestIntegrationViews(APITestCase):
    """Integration testing end points"""

    def setUp(self):
        self.user = create_user()
        RecipeFactory()
        IngredientFactory()

    def test_reset_database(self):
        """It should remove all user created data from the database"""
        self.client.force_authenticate(self.user)
        response = self.client.delete('/api/v1/integration/reset')
        assert response.status_code == status.HTTP_200_OK
        assert len(Recipe.objects.all()) == 0
        assert len(Ingredient.objects.all()) == 0
        assert len(User.objects.all()) == 0

    def test_login_is_required(self):
        response = self.client.delete('/api/v1/integration/reset')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert len(Recipe.objects.all())
        assert len(Ingredient.objects.all())

    def test_only_works_in_debug_mode(self):
        assert False, 'test not written yet'


class TestRestAuthViews(APITestCase):
    """Auth end points"""

    def setUp(self):
        self.user = {
            'username': 'lee',
            'email': 'lee@e.com',
            'password': 'secret'
        }

    def test_login(self):
        """It should allow the user to signup"""
        create_user(**self.user)
        response = self.client.post('/api/v1/rest-auth/login/', format='json',
                                    data=self.user)
        assert response.status_code == status.HTTP_200_OK

    def test_signup(self):
        new_user = {
            'username': 'lee',
            'email': 'lee@e.com',
            'password1': '@secret123',
            'password2': '@secret123'
        }
        response = self.client.post('/api/v1/rest-auth/registration/',
                                    format='json', data=new_user)
        assert response.status_code == status.HTTP_201_CREATED
