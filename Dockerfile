# 1. Use Python image
FROM python:3.9-slim

# 2. Set the folder inside the container
WORKDIR /app

# 3. Install libraries (requests, psycopg2)
# Make sure you have a requirements.txt file!
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy ALL your files (main.py, database.py, config.py)
COPY . .

# 5. Run the boss script
CMD ["python", "main.py"]