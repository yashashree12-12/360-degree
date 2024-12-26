# diet_recommendation/models.py
from django.db import models

class UserProfile(models.Model):
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    weight = models.FloatField()
    height = models.FloatField()
    veg_or_nonveg = models.CharField(max_length=20)
    goal = models.CharField(max_length=50)
    disease = models.TextField(blank=True)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    allergics = models.TextField(blank=True)
    food_type = models.CharField(max_length=100)
    language = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

class DietRecommendation(models.Model):
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    recommendation_text = models.TextField()
    bmi = models.FloatField()
    bmi_category = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)