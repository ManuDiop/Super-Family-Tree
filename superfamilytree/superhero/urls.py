from django.urls import path
from .views import superhero_detail

urlpatterns = [
    path('<int:pk>/', superhero_detail, name='superhero_detail'),
]