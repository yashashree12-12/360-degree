import requests

def get_recommendations(api_key, user_data):
    url =  "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent" # Replace with the actual Gemini API endpoint
    # https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=user_data, headers=headers)
    
    if response.status_code == 200:
        return response.json()  # Assuming the API returns a JSON response
    else:
        response.raise_for_status()
