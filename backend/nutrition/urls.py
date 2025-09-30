from django.urls import path
from .views import score_recipes

urlpatterns = [
    path('score/', score_recipes),
]