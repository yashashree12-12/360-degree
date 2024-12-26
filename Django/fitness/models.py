# models.py
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class FitnessProfile(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ]
    
    FITNESS_LEVEL_CHOICES = [
        ('beginner', 'Beginner (No prior exercise experience)'),
        ('intermediate', 'Intermediate (Exercises 2-3 times/week)'),
        ('advanced', 'Advanced (Regular high-intensity training)')
    ]
    
    ACTIVITY_LEVEL_CHOICES = [
        ('sedentary', 'Sedentary (Little to no exercise)'),
        ('lightly_active', 'Lightly Active (Light exercise 1-3 days/week)'),
        ('moderately_active', 'Moderately Active (Moderate exercise 3-5 days/week)'),
        ('very_active', 'Very Active (Hard exercise 6-7 days/week)'),
        ('extra_active', 'Extra Active (Very hard exercise & physical job)')
    ]
    
    GOAL_CHOICES = [
        ('weight_loss', 'Weight Loss'),
        ('muscle_gain', 'Muscle Gain'),
        ('strength', 'Strength Training'),
        ('endurance', 'Endurance Building'),
        ('flexibility', 'Flexibility & Mobility'),
        ('general_fitness', 'General Fitness'),
        ('maintenance', 'Maintenance')
    ]
    
    EXERCISE_SETTING_CHOICES = [
        ('gym', 'Gym'),
        ('home', 'Home'),
        ('outdoor', 'Outdoor'),
        ('mixed', 'Mixed')
    ]
    
    SLEEP_PATTERN_CHOICES = [
        ('less_than_6', 'Less than 6 hours'),
        ('6_to_8', '6-8 hours'),
        ('more_than_8', 'More than 8 hours')
    ]

    # Basic Information
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    age = models.IntegerField(
        validators=[MinValueValidator(13), MaxValueValidator(100)],
        help_text="Age in years (13-100)"
    )
    gender = models.CharField(
        max_length=10, 
        choices=GENDER_CHOICES
    )
    weight = models.FloatField(
        validators=[MinValueValidator(30), MaxValueValidator(300)],
        help_text="Weight in kg"
    )
    height = models.FloatField(
        validators=[MinValueValidator(100), MaxValueValidator(250)],
        help_text="Height in cm"
    )

    # Fitness Specific Fields
    fitness_level = models.CharField(
        max_length=20,
        choices=FITNESS_LEVEL_CHOICES,
        help_text="Current fitness experience level"
    )
    activity_level = models.CharField(
        max_length=20,
        choices=ACTIVITY_LEVEL_CHOICES,
        help_text="Daily activity level"
    )
    goal = models.CharField(
        max_length=50,
        choices=GOAL_CHOICES,
        help_text="Primary fitness goal"
    )
    specific_area = models.CharField(
        max_length=200,
        help_text="Specific areas you want to focus on (e.g., 'core, upper body')"
    )
    target_timeline = models.CharField(
        max_length=50,
        help_text="Target timeline for achieving your goal"
    )

    # Health Considerations
    medical_conditions = models.TextField(
        blank=True,
        help_text="Any medical conditions that might affect your exercise"
    )
    injuries_or_physical_limitation = models.TextField(
        blank=True,
        help_text="Any injuries or physical limitations to consider"
    )

    # Exercise Environment
    exercise_setting = models.CharField(
        max_length=20,
        choices=EXERCISE_SETTING_CHOICES,
        help_text="Where you plan to exercise"
    )
    available_equipment = models.TextField(
        blank=True,
        help_text="List any exercise equipment you have access to"
    )

    # Lifestyle Factors
    sleep_pattern = models.CharField(
        max_length=20,
        choices=SLEEP_PATTERN_CHOICES,
        help_text="Average daily sleep"
    )
    stress_level = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        help_text="Rate your stress level (1-10)"
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Fitness Profile - {self.goal} - {self.created_at.date()}"

class FitnessRecommendation(models.Model):
    profile = models.ForeignKey(FitnessProfile, on_delete=models.CASCADE)
    recommendation_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    bmi = models.FloatField(null=True)
    bmi_category = models.CharField(max_length=50, null=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Fitness Recommendation for {self.profile.goal} - {self.created_at.date()}"