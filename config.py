import os


class Config:
    # PostgreSQL connection URI format
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:msn%4020@localhost/weatherdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # config.py
    ALERT_THRESHOLDS = {
        "temperature": {
            "high": 35,  # Degrees Celsius
            "consecutive_updates": 2  # Number of consecutive updates
        }
    }
