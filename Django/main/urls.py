from django.urls import path
from . import views

urlpatterns = [
    path('diet/', views.diet_recommendation_view, name='diet_recommendation'),
]
