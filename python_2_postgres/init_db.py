import psycopg2

#Connect to my local Postgress
conn=psycopg2.connect(
    dbname='weather_data',
    user='bunyod',
    password='12345678',
    host='localhost',
    port='5432'
)

cur=conn.cursor()

create_table_query = """
CREATE TABLE IF NOT EXISTS raw_weather (
    id SERIAL PRIMARY KEY,
    city VARCHAR(50),
    temperature FLOAT,
    humidity INT,
    wind_speed FLOAT,
    weather_description VARCHAR(100),
    ingestion_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""
cur.execute(create_table_query)
conn.commit()
cur.close()
conn.close()

print("Table 'raw_weather' created successfully!")