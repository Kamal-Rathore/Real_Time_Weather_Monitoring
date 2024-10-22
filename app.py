
import streamlit as st
from weather_summary import save_daily_summary
from api import get_weather_data
from datetime import datetime
from visualizations import plot_daily_summary  
st.title("Real-Time Weather Monitoring System")


CITIES = ["Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata", "Hyderabad"]


if st.button("Get Weather Data"):
    st.header("Weather Data Summary")
    
    for city in CITIES:
       
        weather_data = get_weather_data(city)
        
        if weather_data:
           
            avg_temp = weather_data['main']['temp']  
            max_temp = weather_data['main']['temp_max']
            min_temp = weather_data['main']['temp_min']
            date = datetime.now().date() 
            dominant_condition = weather_data['weather'][0]['main']

            
            save_daily_summary(date, avg_temp, max_temp, min_temp, dominant_condition)

            
            st.subheader(f"City: {city}")
            st.write(f"**Date:** {date}")
            st.write(f"**Average Temperature:** {avg_temp}°C")
            st.write(f"**Max Temperature:** {max_temp}°C")
            st.write(f"**Min Temperature:** {min_temp}°C")
            st.write(f"**Dominant Weather Condition:** {dominant_condition}")
            st.success(f"Weather data for {city} saved!")
        else:
            st.error(f"Failed to retrieve weather data for {city}.")

   
    st.subheader("Temperature Trends by City")
    plot_daily_summary() 

