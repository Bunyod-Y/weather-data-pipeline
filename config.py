import os

# We use os.getenv so we can read from Docker's environment variables
API_KEY = os.getenv("API_KEY", "11fd0077382cfac1e7a6d05d8c4aab11") 
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "weather_db")
DB_USER = os.getenv("DB_USER", "myuser")
DB_PASS = os.getenv("DB_PASSWORD", "mypassword")