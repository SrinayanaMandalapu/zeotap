
# Weather Monitoring Flask App

This is a real-time weather monitoring system built using Flask and Python. The application retrieves weather data from the OpenWeatherMap API, stores the data in a PostgreSQL database, and generates daily summaries and alerts based on user-defined thresholds.

## Features
- Fetches weather data from OpenWeatherMap API.
- Provides daily weather summaries.
- Allows users to set temperature thresholds.
- Sends alerts when thresholds are breached.

## Project Structure

```bash
weather-monitoring/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── route.py
│   ├── templates/
│   │   ├── index.html
│   │   └── weather.html
│   │   └── weather_summary.html
│   └── utils.py
├── config.py
├── requirements.txt
├── weather.py
└── README.md
```

## Requirements

Install the required packages listed in `requirements.txt`:

```
Flask==2.3.0
SQLAlchemy==1.4.46
psycopg2-binary==2.9.6
requests==2.31.0
python-dotenv==1.0.0
APScheduler==3.9.1
Flask-Migrate

```

You can install the dependencies with:

```bash
pip install -r requirements.txt
```

## Setting up the Database

1. **Configure the database connection**:  
   Update the `SQLALCHEMY_DATABASE_URI` in `config.py` to match your PostgreSQL database details.

   Example:

   ```python
   SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost/dbname'
   ```

2. **Initialize the database**:  
   In your `models.py` file, ensure you have the necessary model definitions for the weather data. You can integrate the database using the `db.create_all()` method as follows:

   ```python
   from app import app, db

   with app.app_context():
       db.create_all()  # This creates all the tables based on the models defined in models.py
   ```

3. Run the above script or place it in your `weather.py` file to initialize the database with all the required tables.



2. **Start the Flask server**:  
   To run the app, execute the following command:

   ```bash
   flask run
   ```

   The server will be available at `http://127.0.0.1:5000`.

## Contributing

Feel free to contribute by submitting issues or pull requests. 

## License

This project is licensed under the MIT License.


                                                                