from django.urls import path, include

from .views import ListRecipe, DetailRecipe

urlpatterns = [
    path('', ListRecipe.as_view()),
    path('<int:pk>/', DetailRecipe.as_view()),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
]
