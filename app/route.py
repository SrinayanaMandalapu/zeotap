from apscheduler.schedulers.background import BackgroundScheduler
from flask import render_template, request
from app import app, db
from app.models import Weather
from app.utils import fetch_weather_data

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    weather_data = fetch_weather_data(city)

    if weather_data:
        # Save weather data to database
        weather = Weather(main=weather_data['main'], 
                          temp=weather_data['temp'],
                          feels_like=weather_data['feels_like'],
                          dt=weather_data['dt'])
        db.session.add(weather)
        db.session.commit()

    return render_template('weather.html', weather_data=weather_data)

@app.route('/show_records', methods= ['GET'])
def show_records():
    weather_records = Weather.query.all()  # Fetch all weather records
    return render_template('show_records.html', weather_records=weather_records)

