from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Recipe
from .serializers import RecipeSerializer


class IntegrationView(APIView):
    """
    Views for integration testing only. Views will only be active in
    development mode
    """

    def delete(self, request, format=None):
        print('this was called')
        return Response()


class ListRecipe(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = (permissions.IsAuthenticated,)


class DetailRecipe(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = (permissions.IsAuthenticated,)
