# Real_Time_Weather_Monitoring

This project is a Real-Time Weather Monitoring System that fetches weather data for several major cities in India (Delhi, Mumbai, Chennai, Bangalore, Kolkata, and Hyderabad) using the OpenWeatherMap API. The data is stored in a MySQL database and visualized using Streamlit and Matplotlib.

# Features:

-> Fetches real-time weather data for selected cities.

-> Saves weather details such as average, max, and min temperatures, and dominant weather conditions.

-> Provides visualizations for weather data trends.

-> Threshold-based alert system for extreme temperatures.

# Project Setup

# 1. Clone the Repository

First, clone the project from GitHub:

git clone https://github.com/Kamal-Rathore/Real-Time-Weather-Monitoring-System.git

cd Real-Time-Weather-Monitoring-System

# 2. Set Up a Virtual Environment

It's a good idea to set up a virtual environment to isolate dependencies:

python -m venv venv

source venv/bin/activate 

# On Windows: venv\Scripts\activate

# 3. Install Dependencies

Install the required Python libraries using requirements.txt:

pip install -r requirements.txt

# 4. Set Up MySQL Database

# 4.1 Install MySQL Server

If MySQL is not installed, download and install MySQL Server.

# 4.2 Create Database and Import MySQL Dump File

To set up the database:

Open MySQL Workbench or any MySQL client.

Create a database named weather_db:

CREATE DATABASE weather_db;

Use the MySQL dump file (weather_db_dump.sql) to load the required schema:

# In MySQL Workbench:

-> Right-click the weather_db database.

-> Select Table Data Import Wizard.

-> Import the provided dump file weather_db_dump.sql (located in the project folder).

Alternatively, in the command line:

mysql -u root -p weather_db < path/to/weather_db_dump.sql

# 5. Configure the API Key

You need an API key from OpenWeatherMap.

-> Sign up for OpenWeatherMap.

-> Get your API key.

-> Open api.py and replace the API_KEY value with your own key:

API_KEY = 'your_openweathermap_api_key'

# 6. Run the Application

Now, run the Streamlit application:


streamlit run app.py

# 7. Using the Application

Once the app runs, follow these steps:

-> Click Get Weather Data to fetch weather information for all cities.

-> The data will be saved to the MySQL database.

-> Graphs displaying the weather trends for each city will be shown.

# 8. Visualize Data

The system automatically plots graphs displaying the daily average temperature for each city. You can view this under the graph section of the Streamlit app.

# File Structure:

app.py: Main Streamlit application.

api.py: Fetches weather data from OpenWeatherMap API.

database.py: Handles MySQL database connections.

weather_summary.py: Saves the weather data into the database.

visualizations.py: Creates and displays visualizations for weather data.

alerts.py: Generates alerts when temperature thresholds are exceeded.

# Troubleshooting

Failed to connect to MySQL?

Ensure that your MySQL server is running, and the credentials in database.py are correct (username, password, etc.).

API not working?

Check if your OpenWeatherMap API key is valid, and ensure you are using the correct URL in api.py.
