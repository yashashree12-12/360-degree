# diet_recommendation/views.py
from django.shortcuts import render
from .forms import DietRecommendationForm
from .models import UserProfile, DietRecommendation  # Add this import
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

def diet_recommendation_view(request):
    if request.method == 'POST':
        form = DietRecommendationForm(request.POST)
        if form.is_valid():
            profile = form.save()
            
            # Calculate BMI
            bmi, bmi_category = calculate_bmi(float(profile.weight), float(profile.height))
            
            # Configure the API key
            genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
            
            # Create the model
            model = genai.GenerativeModel("gemini-pro")

            prompt = f"""
            Create a structured, easy-to-read diet and wellness plan with clear numbering (no markdown).
            Use simple numbering (1., 2., 3.) and clear section breaks.
            Format the response as plain text with clear headings and proper spacing.

            Create a plan for someone with these details:
            Age: {profile.age}
            Gender: {profile.gender}
            Weight: {profile.weight} kg
            Height: {profile.height} cm
            Diet Type: {profile.veg_or_nonveg}
            Goal: {profile.goal}
            Health Conditions: {profile.disease}
            Location: {profile.country}, {profile.state}
            Food Allergies: {profile.allergics}
            Food Preference: {profile.food_type}
            Language: {profile.language}

            Format the response in this exact structure:

            PERSONAL DIET AND WELLNESS PLAN
            ===============================

            1. PROFILE SUMMARY
               -------------
               [List key details about the person]

            2. DAILY NUTRITION TARGETS
               ---------------------
               a) Calories:
               b) Protein:
               c) Carbs:
               d) Fats:

            3. MEAL SCHEDULE
               -------------
               BREAKFAST:
               - Item 1 (portion)
               - Item 2 (portion)

               MORNING SNACK:
               - Item 1 (portion)
               - Item 2 (portion)

               LUNCH:
               - Item 1 (portion)
               - Item 2 (portion)

               EVENING SNACK:
               - Item 1 (portion)
               - Item 2 (portion)

               DINNER:
               - Item 1 (portion)
               - Item 2 (portion)

            4. WEEKLY WORKOUT PLAN
               -----------------
               [Day-wise exercise plan]

            5. FOODS TO INCLUDE
               ---------------
               [List essential foods]

            6. FOODS TO AVOID
               -------------
               [List foods to avoid]

            7. LIFESTYLE RECOMMENDATIONS
               ------------------------
               [List key lifestyle tips]

            8. IMPORTANT NOTES
               --------------
               [Any specific considerations based on health conditions or allergies]

            Use clear spacing and numbering. No markdown formatting.
            """

            response = model.generate_content(prompt)
            recommendation_text = response.text

            response = model.generate_content(prompt)
            recommendation_text = response.text.replace('```', '').replace('#', '')

            # Save recommendation
            diet_recommendation = DietRecommendation.objects.create(
                profile=profile,
                recommendation_text=recommendation_text,
                bmi=bmi,
                bmi_category=bmi_category
            )

            return render(request, 'main/recommendation_result.html', {
                'recommendation': recommendation_text,
                'bmi': bmi,
                'bmi_category': bmi_category,
                'profile': profile
            })
    else:
        form = DietRecommendationForm()

    return render(request, 'main/recommendation_form.html', {'form': form})
