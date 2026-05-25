from fastapi import FastAPI
import requests

app = FastAPI()

API_KEY = "4fc483e4694584deee81da46cef64055"

@app.get("/")
def home():
    return {"message": "Weather API Project"}

@app.get("/weather/{city}")
def get_weather(city: str):

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)

    data = response.json()

    print(data)

    # Handle API errors
    if response.status_code != 200:
        return {
            "status": "error",
            "message": data.get("message")
        }

    return {
        "city": city,
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "weather": data["weather"][0]["description"],
        "wind_speed": data["wind"]["speed"]
    }