Weather Info App:

This is my first project. A simple and responsive weather application built with Flask that provides real-time weather information for any city using the OpenWeather API.

Live Demo:

Live Website: https://weather-app-1-p6ea.onrender.com

Technologies Used:

Python
Flask
HTML5
CSS3
OpenWeather API
Requests
Gunicorn
Git & GitHub
Render

Project Structure:

Weather-App/
│
├── static/
│   └── css/
│       └── style.css
│
├── templates/
│   └── index.html
│
├── app.py
├── requirements.txt
├── .gitignore
├── .env (not comitted on git)
└── README.md

Installation:

Clone the repository:

git clone https://github.com/Anujpawar05/Weather-App.git

Go into the project:

cd Weather-App

Create a virtual environment:

python -m venv .venv

Activate the virtual environment.

Windows (PowerShell):

.\.venv\Scripts\Activate.ps1

Install the dependencies:

pip install -r requirements.txt

Create a .env file:

OPENWEATHER_API_KEY=YOUR_API_KEY

Run the application:

python app.py

Open your browser:

http://127.0.0.1:5000

Future features:

Weather icons
Current location support
Search history

