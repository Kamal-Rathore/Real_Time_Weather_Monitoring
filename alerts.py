def check_alerts(current_temp,threshold):
    if current_temp > threshold:
        print(f"Alert: Temperature exceeded threshold current temperature is: {current_temp}°C")
        
