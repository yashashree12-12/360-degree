# diet_recommendation/forms.py
from django import forms
from .models import UserProfile

class DietRecommendationForm(forms.ModelForm):
    GENDER_CHOICES = [('Male', 'Male'), ('Female', 'Female')]
    DIET_CHOICES = [('Veg', 'Veg'), ('Non-Veg', 'Non-Veg'), ('Veg & Non-Veg', 'Veg & Non-Veg')]
    GOAL_CHOICES = [
        ('Gain muscles', 'Gain muscles'),
        ('Lose weight', 'Lose weight'),
        ('Maintain physique', 'Maintain physique')
    ]
    LANGUAGE_CHOICES = [
        ("English", "English"), ("Hindi", "Hindi"), ("Bengali", "Bengali"),
        ("Punjabi", "Punjabi"), ("Tamil", "Tamil"), ("Telugu", "Telugu"),
        ("Urdu", "Urdu"), ("Spanish", "Spanish"), ("French", "French"),
        ("German", "German")
    ]

    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    veg_or_nonveg = forms.ChoiceField(choices=DIET_CHOICES)
    goal = forms.ChoiceField(choices=GOAL_CHOICES)
    language = forms.ChoiceField(choices=LANGUAGE_CHOICES)

    class Meta:
        model = UserProfile
        exclude = ['created_at']
        widgets = {
            'disease': forms.Textarea(attrs={'rows': 3}),
            'allergics': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-green-500 focus:ring-green-500'
            })