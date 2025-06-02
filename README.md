# EN OpenWeather ETL Pipeline with Airflow

This project is a simple ETL pipeline that uses **Apache Airflow** to extract weather data from (Europe Only countries), transform it, and load it into a **PostgreSQL** database.

<img width="618" alt="image" src="https://github.com/user-attachments/assets/165b1b52-d592-4819-9694-328c952faf73" />


## Stack Used

- Apache Airflow → For orchestration and to run the ETL every hour
- PostgreSQL → Database to store the structured weather data (connected to DBeaver for easier inspection and manipulation)
- Docker → Containerizes the entire environment for consistent and reproducible setup
- OpenWeatherMap API → Source of real-time weather data for European cities
- Python (requests, pandas) → Used to extract data from the API, structure it, and handle CSV operations

## Features

- The ETL runs every 1 hour
- Extracts current weather data for all European cities
- Save raw data as CSV
- Load structured data into PostgreSQL

## DAG Behavior

- Runs every hour (`@hourly`)
- Extracts data from the API
- Writes to a CSV file
- Loads data into `open_weather.open_weather_api_tbl` in Postgres

  <img width="959" alt="image" src="https://github.com/user-attachments/assets/fb326516-3f34-4404-8cee-ebe25cdd2f26" />

## PostgreSQL Table
`open_weather.open_weather_api_tbl` stores the following:

<img width="959" alt="image" src="https://github.com/user-attachments/assets/4d8f9102-47ef-4777-b535-23bf478020e7" />

---

# 🇫🇷 OpenWeather ETL Pipeline avec Airflow

Ce projet est un pipeline ETL simple qui utilise **Apache Airflow** pour extraire des données météo via l'**API OpenWeatherMap**, les transformer et les charger dans une base de données **PostgreSQL**.

## Technologies utilisées

- Apache Airflow → Pour l’orchestration et l'exécution automatique de l’ETL chaque heure
- PostgreSQL → Base de données pour stocker les données météo structurées (connectée à DBeaver pour une manipulation facile)
- Docker → Conteneurise l’environnement pour un déploiement cohérent et reproductible
- API OpenWeatherMap → Source des données météo en temps réel pour les villes européennes
- Python (requests, pandas) → Utilisé pour extraire les données de l’API, les structurer et gérer les fichiers CSV

## Fonctionnalités

- ETL planifié chaque heure
- Extraction de données météo pour plusieurs villes européennes
- Sauvegarde des données dans un fichier CSV
- Chargement structuré dans PostgreSQL

## Comportement du DAG

- S'exécute chaque heure (`@hourly`)
- Extrait les données de l'API
- Sauvegarde en CSV
- Charge les données dans la table `open_weather.open_weather_api_tbl` de Postgres

<img width="959" alt="image" src="https://github.com/user-attachments/assets/fb326516-3f34-4404-8cee-ebe25cdd2f26" />

## Table PostgreSQL 
`open_weather.open_weather_api_tbl` enregistre:

<img width="959" alt="image" src="https://github.com/user-attachments/assets/4d8f9102-47ef-4777-b535-23bf478020e7" />
