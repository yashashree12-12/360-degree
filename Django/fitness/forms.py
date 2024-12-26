# forms.py
from django import forms
from .models import FitnessProfile

class FitnessRecommendationForm(forms.ModelForm):
    class Meta:
        model = FitnessProfile
        exclude = ['created_at', 'updated_at']
        widgets = {
            'age': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your age'
            }),
            'gender': forms.Select(attrs={
                'class': 'form-control'
            }),
            'weight': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Weight in kg'
            }),
            'height': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Height in cm'
            }),
            'fitness_level': forms.Select(attrs={
                'class': 'form-control'
            }),
            'activity_level': forms.Select(attrs={
                'class': 'form-control'
            }),
            'goal': forms.Select(attrs={
                'class': 'form-control'
            }),
            'specific_area': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., core strength, upper body, legs'
            }),
            'target_timeline': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., 3 months, 6 months'
            }),
            'medical_conditions': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'List any medical conditions that might affect your exercise'
            }),
            'injuries_or_physical_limitation': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Describe any injuries or physical limitations'
            }),
            'exercise_setting': forms.Select(attrs={
                'class': 'form-control'
            }),
            'available_equipment': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'List equipment you have access to'
            }),
            'sleep_pattern': forms.Select(attrs={
                'class': 'form-control'
            }),
            'stress_level': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 1,
                'max': 10,
                'placeholder': 'Rate from 1-10'
            })
        }

    def clean(self):
        cleaned_data = super().clean()
        
        # Validate age
        age = cleaned_data.get('age')
        if age and (age < 13 or age > 100):
            raise forms.ValidationError('Age must be between 13 and 100 years.')
        
        # Validate weight
        weight = cleaned_data.get('weight')
        if weight and (weight < 30 or weight > 300):
            raise forms.ValidationError('Weight must be between 30 and 300 kg.')
        
        # Validate height
        height = cleaned_data.get('height')
        if height and (height < 100 or height > 250):
            raise forms.ValidationError('Height must be between 100 and 250 cm.')
        
        # Validate stress level
        stress_level = cleaned_data.get('stress_level')
        if stress_level and (stress_level < 1 or stress_level > 10):
            raise forms.ValidationError('Stress level must be between 1 and 10.')

        return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add any initialization if needed
        self.fields['medical_conditions'].required = False
        self.fields['injuries_or_physical_limitation'].required = False
        self.fields['available_equipment'].required = False