from django.urls import path
from . import views

urlpatterns = [
    path('', views.fitness_recommendation_view, name='fitness_recommendation'),
]
