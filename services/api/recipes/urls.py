from django.urls import path

from .views import ListRecipe, DetailRecipe

urlpatterns = [
    path('', ListRecipe.as_view()),
    path('<int:pk>/', DetailRecipe.as_view()),
]
