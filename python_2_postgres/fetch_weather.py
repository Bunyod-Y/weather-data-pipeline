import requests
import psycopg2
import sys

# --- CONFIGURATION ---
# Replace this with your actual Weatherstack API Key
API_KEY = "YOUR_API_KEY_HERE" # I removed my real key for GitHub security 
CITY = "Tashkent"
# This URL matches the data format you showed me
URL = f"http://api.weatherstack.com/current?access_key={API_KEY}&query={CITY}"

def fetch_and_load_weather():
    try:
        # 1. Extract (Fetch data from API)
        print(f"Fetching weather for {CITY}...")
        response = requests.get(URL)
        response.raise_for_status()
        data = response.json()

        # Debugging: Uncomment the next line if you get another error
        # print("DEBUG:", data)

        # Check if the API returned an error (like invalid key)
        if 'success' in data and data['success'] is False:
            print(f"API Error: {data['error']['info']}")
            return

        # 2. Parse key fields (Matched to your JSON)
        # Your data is inside 'current', not 'main'
        current_data = data['current']

        temp = current_data['temperature']
        humidity = current_data['humidity']
        wind_speed = current_data['wind_speed']  # <--- This was the fix (it is wind_speed, not speed)
        
        # 'weather_descriptions' is a list like ['Mist'], so we take the first item [0]
        desc = current_data['weather_descriptions'][0]
        
        # 3. Load (Save to Postgres)
        conn = psycopg2.connect(
            dbname="weather_data",
            user="bunyod",
            password="12345678",
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()
        
        insert_query = """
        INSERT INTO raw_weather (city, temperature, humidity, wind_speed, weather_description)
        VALUES (%s, %s, %s, %s, %s);
        """
        
        cur.execute(insert_query, (CITY, temp, humidity, wind_speed, desc))
        conn.commit()
        
        print(f"✅ Successfully loaded data for {CITY}: {temp}°C, {desc}, Wind: {wind_speed} km/h")
        
        cur.close()
        conn.close()

    except KeyError as e:
        print(f"❌ Key Error: Missing field {e} in the API response.")
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    fetch_and_load_weather()