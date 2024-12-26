# diet_recommendation/views.py
from django.shortcuts import render
from .forms import FitnessRecommendationForm
from .models import FitnessProfile, FitnessRecommendation   # Add this import
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

def calculate_bmi(weight, height):
    height_m = height / 100.0
    bmi = weight / (height_m ** 2)
    
    if bmi < 18.5:
        category = 'Underweight'
    elif 18.5 <= bmi < 24.9:
        category = 'Normal weight'
    elif 25 <= bmi < 29.9:
        category = 'Overweight'
    else:
        category = 'Obesity'
    
    return bmi, category

def fitness_recommendation_view(request):
    if request.method == 'POST':
        form = FitnessRecommendationForm(request.POST)
        if form.is_valid():
            profile = form.save()
            
            # Calculate BMI
            bmi, bmi_category = calculate_bmi(float(profile.weight), float(profile.height))
            
            # Configure the API key
            genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
            
            # Create the model
            model = genai.GenerativeModel("gemini-pro")
                                
            prompt = f"""
            As an expert fitness trainer, create a comprehensive, personalized fitness plan in this exact structure:

           
            "user_profile": 
                "personal_info": 
                    "age": {profile.age},
                    "gender": "{profile.gender}",
                    "current_weight": {profile.weight},
                    "height": {profile.height},
                    "health_goal": "{profile.goal}",
                    "physical_limitations": "{profile.injuries_or_physical_limitation}",
                    "fitness_level": "{profile.fitness_level}",
                    "activity_level": "{profile.activity_level}",
                    "target_timeline": "{profile.target_timeline}",
                    "exercise_setting": "{profile.exercise_setting}",
                    "sleep_pattern": "{profile.sleep_pattern}",
                    "focus_areas": "{profile.specific_area}"
         
            ----------------------------------------------------------------------------
            Generate a personalized fitness plan that:
            1. Accounts for the age ({profile.age}) and gender ({profile.gender})
            3. Adapts for injuries/limitations: {profile.injuries_or_physical_limitation}
            4. Matches fitness level: {profile.fitness_level}
            5. Aligns with activity level: {profile.activity_level}
            6. Focuses on target areas: {profile.specific_area}
            7. Provides progression for: {profile.target_timeline}
            8. Works with available setting: {profile.exercise_setting}
            9. Accounts for sleep pattern: {profile.sleep_pattern}

            ----------------------------------------------------------------------------
            Ensure the plan:
            - Includes detailed exercise descriptions
            - Provides alternative exercises for each movement
            - Includes proper warm-up and cool-down routines
            - Addresses any medical conditions or injuries
            - Gives clear progression guidelines
            - Includes safety precautions
            - Matches the user's available equipment
            - Provides modifications for different fitness levels
            - Includes recovery protocols
            - Has clear tracking metrics

            ----------------------------------------------------------------------------

            The exercises should be:
            1. Appropriate for the user's fitness level
            2. Achievable in the specified setting
            3. Safe considering any medical conditions
            4. Progressive over the timeline
            5. Focused on the specified target areas
            6. Balanced to prevent overuse injuries
            7. Adaptable based on available equipment

            Please format the response in a clean, easy-to-read format without markdown symbols.
            give spaces after each block of information.
            """

            # response = model.generate_content(prompt)
            # recommendation_text = response.text

            response = model.generate_content(prompt)
           # In views.py
            recommendation_text = response.text.replace('*', '').replace('#', '').replace('```', '')
            

            # Save recommendation
            fitness_recommendation = FitnessRecommendation.objects.create(
                profile=profile,
                recommendation_text=recommendation_text,
                bmi=bmi,
                bmi_category=bmi_category
            )

            return render(request, 'fitness/result.html', {
                'recommendation': recommendation_text,
                'bmi': bmi,
                'bmi_category': bmi_category,
                'profile': profile
            })
    else:
        form = FitnessRecommendationForm()

    return render(request, 'fitness/form.html', {'form': form})