import requests
import os
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()
app_id = os.environ.get('APP_ID')
api_key = os.environ.get('API_KEY')
sheety_authorization = os.environ.get('SHEETY_AUTHORIZATION')
exercise_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
sheet_endpoint = 'https://api.sheety.co/6e46dcf33f155c3a29e2aeb53bfbd031/workout/workouts'
exercise_input = input("Tell me which exercise did you do today?: ")
header = {
    "x-app-id": app_id,
    "x-app-key": api_key,
}
sheety_header = {
    'Authorization': sheety_authorization,
}


parameters = {
    'query': exercise_input,
    'gender': 'male',
    'weight_kg': 60,
    'height_cm': 172,
    'age': 30,
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=header)
response.raise_for_status()
results = response.json()

today_date = datetime.now().strftime('%d/%m/%Y')
now_time = datetime.now().strftime('%X')


for result in results['exercises']:
    sheet_input = {
        'workout': {
            'date': today_date,
            'time': now_time,
            'exercise': result['user_input'].title(),
            'duration': result['duration_min'],
            'calories': result['nf_calories'],
        }
    }

    response = requests.post(sheet_endpoint, json=sheet_input, headers=sheety_header)
    print(response.text)
































# for future purpose in case you need the code for calory count for each day (more relevant to you)
#food_input = input("Tell me what did you eat & drink today?: ")
#calorie_endpoint = 'https://trackapi.nutritionix.com/v2/natural/nutrients'
# parameters = {
#     'query': food_input,
# }
#
# response = requests.post(url=calorie_endpoint, json=parameters, headers=header)
# response.raise_for_status()
# result = response.json()
# results = result['foods']
#
# total_calorie = 0
# for result in results:
#     cal = result['nf_calories']
#     total_calorie += cal
# print(total_calorie)





