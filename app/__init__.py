from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#from crontab import CronTab

app = Flask(__name__)
app.config.from_object('config.Config')

db = SQLAlchemy(app)
#cron = CronTab(user='manda')


