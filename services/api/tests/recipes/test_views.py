"""recipes views test suite"""
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User


def create_user(username, email, password):
    """Creates a user for testing purposes"""
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


class TestRestAuthViews(APITestCase):
    """Auth end points"""

    def setUp(self):
        self.user = {
            'username': 'lee',
            'email': 'lee@e.com',
            'password': 'secret'
        }

    def tearDown(self):
        User.objects.all().delete()

    def test_login(self):
        """It should allow the user to signup"""
        create_user(**self.user)
        response = self.client.post('/api/v1/rest-auth/login/', format='json',
                                    data=self.user)
        assert response.status_code == status.HTTP_200_OK

    def test_signup(self):
        response = self.client.post('/api/v1/rest-auth/signup/', format='json',
                                    data=self.user)
        assert response.status_code == status.HTTP_200_OK
