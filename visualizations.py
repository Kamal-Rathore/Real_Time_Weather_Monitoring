
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
from database import connect_to_db

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
from database import connect_to_db

def plot_daily_summary():
   
    db = connect_to_db()
    query = "SELECT date, city, avg_temp, max_temp, min_temp, dominant_condition FROM daily_summaries"
    df = pd.read_sql(query, db)
    
    if not df.empty:
       
        fig, axs = plt.subplots(2, 2, figsize=(15, 10))
        
      
        sns.lineplot(data=df, x='date', y='avg_temp', hue='city', ax=axs[0, 0], marker='o')
        axs[0, 0].set_title('Average Temperature by City')
        axs[0, 0].set_xlabel('Date')
        axs[0, 0].set_ylabel('Avg Temperature (°C)')
        axs[0, 0].tick_params(axis='x', rotation=45)

       
        sns.lineplot(data=df, x='date', y='max_temp', hue='city', ax=axs[0, 1], marker='o')
        axs[0, 1].set_title('Max Temperature by City')
        axs[0, 1].set_xlabel('Date')
        axs[0, 1].set_ylabel('Max Temperature (°C)')
        axs[0, 1].tick_params(axis='x', rotation=45)

        
        sns.lineplot(data=df, x='date', y='min_temp', hue='city', ax=axs[1, 0], marker='o')
        axs[1, 0].set_title('Min Temperature by City')
        axs[1, 0].set_xlabel('Date')
        axs[1, 0].set_ylabel('Min Temperature (°C)')
        axs[1, 0].tick_params(axis='x', rotation=45)

      
        sns.countplot(data=df, x='dominant_condition', hue='city', ax=axs[1, 1])
        axs[1, 1].set_title('Dominant Weather Condition by City')
        axs[1, 1].set_xlabel('Dominant Condition')
        axs[1, 1].set_ylabel('Count')

       
        plt.tight_layout()

       
        st.pyplot(fig)
    else:
        st.write("No data available for plotting.")

def load_weather_data():
    db = connect_to_db()
    query = "SELECT city, date, avg_temp FROM daily_summaries"
    df = pd.read_sql(query, db)
    db.close()
    return df

def plot_heatmap():
    df = load_weather_data()

    if not df.empty:
        df_pivot = df.pivot(index='date', columns='city', values='avg_temp')

        plt.figure(figsize=(10, 6))
        
      
        sns.heatmap(df_pivot, annot=True, fmt=".1f", cmap="YlGnBu", linewidths=0.5, linecolor="gray")

  
        plt.title('Heatmap of Average Temperatures by City and Date', fontsize=16, fontweight='bold')
        plt.xlabel('City', fontsize=12)
        plt.ylabel('Date', fontsize=12)

       
        plt.tight_layout()

   
        st.pyplot(plt.gcf())
    else:
        st.write("No data available for plotting.")
