from django.contrib import admin

# Register your models here.
from .models import UserProfile
from .models import DietRecommendation

# Register the model
admin.site.register(UserProfile)
admin.site.register(DietRecommendation)