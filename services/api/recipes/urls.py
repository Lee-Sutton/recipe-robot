from django.urls import path, include

from .views import ListRecipe, DetailRecipe, IntegrationView

urlpatterns = [
    path('integration/reset', IntegrationView.as_view()),
    path('', ListRecipe.as_view()),
    path('<int:pk>/', DetailRecipe.as_view()),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
]
