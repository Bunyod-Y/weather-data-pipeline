# 🌤️ End-to-End Weather ELT Pipeline

A robust, containerized data pipeline that extracts real-time weather data, loads it into a warehouse, transforms it using dbt, and orchestrates the workflow with Airflow.

![Architecture Diagram]

<img width="2816" height="1536" alt="Gemini_Generated_Image_7jcy087jcy087jcy" src="https://github.com/user-attachments/assets/4ba5bb54-2b2a-44a4-91a7-7305c939b03c" />



## 🚀 Project Overview
This project demonstrates a modern **ELT (Extract, Load, Transform)** architecture completely built on a local machine using Docker. It mimics a production-grade data engineering environment.

* **Extract:** Python script hits the OpenWeatherMap API.
* **Load:** Raw JSON data is loaded into **PostgreSQL** (Docker).
* **Transform:** **dbt (data build tool)** models clean, cast, and derive new metrics (e.g., Fahrenheit conversion) in the `analytics` schema.
* **Orchestrate:** **Apache Airflow** (via Astro CLI) schedules and manages dependencies between tasks.
* **Visualize:** **Metabase** connects to the transformed data for dashboarding.

## 🛠️ Tech Stack
* **Containerization:** Docker & Docker Compose
* **Orchestration:** Apache Airflow 3 (running on Astro Runtime)
* **Transformation:** dbt Core (postgres adapter)
* **Data Warehouse:** PostgreSQL
* **Language:** Python 3.12+
* **Visualization:** Metabase

## 📂 Project Structure
```text
├── airflow_orchestration/
│   ├── dags/
│   │   ├── fetch_weather.py      # Extract & Load script
│   │   ├── weather_dag.py        # Airflow DAG definition
│   │   └── weather_transform/    # dbt project folder
│   ├── Dockerfile                # Astro/Airflow image config
│   └── requirements.txt          # Python dependencies
├── .gitignore
└── README.md
