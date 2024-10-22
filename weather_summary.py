from datetime import datetime
from database import connect_to_db
def save_daily_summary(date, avg_temp, max_temp, min_temp, dominant_condition):
    db = connect_to_db()
    cursor = db.cursor()
    cursor.execute("""
        INSERT INTO daily_summaries (date, avg_temp, max_temp, min_temp, dominant_condition) 
        VALUES (%s, %s, %s, %s, %s)
    """, (date, avg_temp, max_temp, min_temp, dominant_condition))
    db.commit()
    cursor.close()
    db.close()
