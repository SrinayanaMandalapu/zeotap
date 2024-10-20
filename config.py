import os
from dotenv import load_dotenv
load_dotenv()
class Config:
    # PostgreSQL connection URI format
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # config.py
    ALERT_THRESHOLDS = {
        "temperature": {
            "high": 35,  # Degrees Celsius
            "consecutive_updates": 2  # Number of consecutive updates
        }
    }
