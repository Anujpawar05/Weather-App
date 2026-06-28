from dotenv import load_dotenv
import os
from flask import Flask, render_template, request
import requests
from requests.exceptions import RequestException

# Load environment variables from .env
load_dotenv()

app = Flask(__name__)

# Get API key from .env
API_KEY = os.getenv("OPENWEATHER_API_KEY")


@app.route("/", methods=["GET", "POST"])
def home():
    weather_data = None
    error = None

    if request.method == "POST":
        city = request.form["city"].strip()

        if not city:
            error = "Please enter a city name."
        elif not API_KEY:
            error = "Weather API key is not configured."
        else:
            url = (
                f"https://api.openweathermap.org/data/2.5/weather"
                f"?q={city}&appid={API_KEY}&units=metric"
            )

            try:
                response = requests.get(url, timeout=10)
                data = response.json()

                if response.status_code != 200:
                    error = data.get("message", "Error fetching weather.")
                else:
                    weather_data = {
                        "city": data["name"],
                        "temp": data["main"]["temp"],
                        "humidity": data["main"]["humidity"],
                        "wind": data["wind"]["speed"],
                        "condition": data["weather"][0]["description"].title()
                    }

            except RequestException:
                error = "Unable to connect to the weather service. Please try again later."

    return render_template("index.html", weather=weather_data, error=error)


if __name__ == "__main__":
    app.run()