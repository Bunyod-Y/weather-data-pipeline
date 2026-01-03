import psycopg2
import time  # <--- Added this
from config import DB_HOST, DB_NAME, DB_USER, DB_PASS

def get_connection():
    # Try to connect 5 times, waiting 2 seconds between tries
    for i in range(5):
        try:
            conn = psycopg2.connect(
                host=DB_HOST,
                database=DB_NAME,
                user=DB_USER,
                password=DB_PASS
            )
            return conn
        except psycopg2.OperationalError:
            print(f"⏳ Database not ready... waiting 2 seconds (Attempt {i+1}/5)")
            time.sleep(2)
    
    # If we get here, we failed 5 times
    raise Exception("❌ Could not connect to Database after 5 retries.")

def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS weather_data (
            id SERIAL PRIMARY KEY,
            city VARCHAR(50),
            temperature INT,
            humidity INT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)
    conn.commit()
    cursor.close()
    conn.close()
    print("✅ Table checked/created.")

def insert_weather(city, temp, humidity):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO weather_data (city, temperature, humidity) VALUES (%s, %s, %s)",
        (city, temp, humidity)
    )
    conn.commit()
    cursor.close()
    conn.close()
    print(f"✅ Saved data for {city} to Database.")