import requests
import datetime
from app import db, app
from app.models import Weather

high_temp_count = 0
ALERT_THRESHOLD = 35

def fetch_weather_data(city):
    global high_temp_count  # Use the global count variable
    with app.app_context():
        api_key = '82d1136e27fc8eca88ad15a166defb96'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            dt_datetime = datetime.datetime.fromtimestamp(data['dt'])

            # Preparing data to save in the database
            new_data = {
                'main': data['weather'][0]['main'],  # Weather condition
                'temp': data['main']['temp'],  # Current temperature in Kelvin
                'feels_like': data['main']['feels_like'],  # Feels like temperature in Kelvin
                'dt': dt_datetime, # Timestamp of the weather data
                'city':city
            }

            # Creating a new Weather instance
            new_weather = Weather(**new_data)

            # Adding the new weather data to the session and committing to the database
            db.session.add(new_weather)
            db.session.commit()
            print(f'{city} Uploaded successfully')

            # Check temperature against the threshold and update the count
            current_temp_celsius = new_data['temp'] - 273.15  # Convert Kelvin to Celsius
            if current_temp_celsius > ALERT_THRESHOLD:
                high_temp_count += 1
            else:
                high_temp_count = 0  # Reset count if temperature is below the threshold

            # Trigger an alert if count exceeds 2
            if high_temp_count > 2:
                alert_message = ("High temperature alert! The temperature has exceeded the threshold for consecutive "
                                 "readings.")
                print(alert_message)
                return new_data, alert_message

            return new_data, None

        print(f"Error fetching data: {response.status_code} - {response.text}")
        return None, None
