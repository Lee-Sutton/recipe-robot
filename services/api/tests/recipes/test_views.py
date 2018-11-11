"""recipes views test suite"""
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User


def create_user(username, email, password):
    user = User(username=username, email=email)
    user.set_password(password)
    user.save()
    return user


class TestRecipeViews(APITestCase):
    """Recipe rest endpoints"""

    def test_recipe_list(self):
        """it should return a list of recipes in the database"""
        user = create_user('lee', 'lee@e.com', 'secret')
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
