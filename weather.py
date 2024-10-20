import psycopg2
from flask import render_template, request, jsonify
from app import app, db
#from app.models import Weather
from app.utils import fetch_weather_data
import time
from flask_migrate import Migrate
from app import db
from datetime import datetime
import datetime
from datetime import datetime
from flask_apscheduler import APScheduler

scheduler = APScheduler()
app.config.from_object('config.Config')


#migrate = Migrate(app, db)

class Weather(db.Model):
    __tablename__ = "weather"
    __table_args__ = {'extend_existing':True}
    id = db.Column(db.Integer, primary_key=True)
    main = db.Column(db.String(50))
    temp = db.Column(db.Float)
    feels_like = db.Column(db.Float)
    dt = db.Column(db.DateTime, default=datetime.utcnow)
    city = db.Column(db.String(50))

    def __repr__(self):
        return f'<Weather {self.main}>'
with app.app_context():
    db.create_all()

def schedule_jobs():
    scheduler.add_job(
        id='Delhi',
        func=fetch_weather_data,
        trigger='interval',
        seconds=30,
        args=['Delhi']
    )
    scheduler.add_job(
        id='Hyderabad',
        func=fetch_weather_data,
        trigger='interval',
        seconds=30,
        args=['Hyderabad']
    )
    scheduler.add_job(
        id='Kolkata',
        func=fetch_weather_data,
        trigger='interval',
        seconds=30,
        args=['Kolkata']
    )
    scheduler.add_job(
        id='Chennai',
        func=fetch_weather_data,
        trigger='interval',
        seconds=30,
        args=['Chennai']
    )
    scheduler.add_job(
        id='Mumbai',
        func=fetch_weather_data,
        trigger='interval',
        seconds=30,
        args=['Mumbai']
    )
    scheduler.add_job(
        id='Bangalore',
        func=fetch_weather_data,
        trigger='interval',
        seconds=30,
        args=['Bangalore']
    )


scheduler.init_app(app)


def get_db_connection():
    conn = psycopg2.connect(
        host='localhost',
        database='weatherdb',
        user='postgres',
        password='msn@20'
    )
    return conn


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    weather_data, alert_message = fetch_weather_data(city)

    if weather_data:
        # Save weather data to database
        weather = Weather(main=weather_data['main'],
                          temp=weather_data['temp'],
                          feels_like=weather_data['feels_like'],
                          dt=weather_data['dt'],
                          city=city)
        db.session.add(weather)
        db.session.commit()

    return render_template('weather.html', weather_data=weather_data, city=city)


@app.route('/weather_summary', methods=['GET', 'POST'])
def temperature():
    if request.method == 'POST':

        today_date = datetime.now().strftime('%Y-%m-%d')

        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute("""
                    SELECT 
                        MIN(temp)-273.15 AS min_temp, 
                        MAX(temp)-273.15 AS max_temp, 
                        AVG(temp)-273.15 AS avg_temp, 
                        main 
                    FROM weather 
                    WHERE DATE(dt) = %s 
                    GROUP BY main 
                    ORDER BY COUNT(main) DESC 
                    LIMIT 1;  -- Get the most frequent main condition
                """, (today_date,))
        result = cur.fetchone()
        cur.close()
        conn.close()

        if result:
            min_temp, max_temp, avg_temp, most_frequent_main = result
        else:
            min_temp = max_temp = avg_temp = most_frequent_main = None

        return render_template('weather_summary.html',
                               date=today_date,
                               min_temp=min_temp,
                               max_temp=max_temp,
                               avg_temp=avg_temp,
                               most_frequent_main=most_frequent_main)

    # If it's a GET request, you can directly render the summary page or the index page
    return render_template('index.html')


@app.route('/visualizations')
def visualizations():
    return render_template('visualizations.html')


if __name__ == "__main__":
    # Schedule the task
    schedule_jobs()

    # Start the scheduler
    scheduler.start()

    # Run the Flask app
    app.run(debug=True)
