from django.urls import path
from .views import superhero_detail, add_superhero

urlpatterns = [
    path('<int:pk>/', superhero_detail, name='superhero_detail'),
    path('add/', add_superhero, name='add_superhero'),
]