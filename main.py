import requests
import sys
from config import API_KEY
# Importing functions from your other file!
from database import create_table, insert_weather 

BASE_URL = "http://api.weatherstack.com/current"

def fetch_api_data(city):
    print(f"🌍 Fetching weather for {city}...")
    params = {
        'access_key': API_KEY,
        'query': city
    }
    
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()
        
        if 'error' in data:
            print(f"❌ API Error: {data['error']['info']}")
            return None
            
        return data
    except Exception as e:
        print(f"❌ Error fetching data: {e}")
        return None

if __name__ == "__main__":
    # 1. Setup DB
    create_table()
    
    # 2. Get Data
    city_name = "New York"
    weather_data = fetch_api_data(city_name)
    
    # 3. Save Data (Only if API call was successful)
    if weather_data:
        current = weather_data['current']
        # Call the function from database.py
        insert_weather(
            city=city_name,
            temp=current['temperature'],
            humidity=current['humidity']
        )