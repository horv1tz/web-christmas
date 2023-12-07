from fastapi import FastAPI
from datetime import datetime, timedelta

app = FastAPI()

def time_until_new_year():
    now = datetime.now()
    new_year = datetime(now.year + 1, 1, 1)
    time_delta = new_year - now
    
    days = time_delta.days
    hours, remainder = divmod(time_delta.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    time = {
        "days": days,
        "hours": hours,
        "minutes": minutes,
        "seconds": seconds,
    }

    return time


@app.get("/christmas")
def get_time_until_new_year():
    time_left = time_until_new_year()
    return {"time_until": time_left}
