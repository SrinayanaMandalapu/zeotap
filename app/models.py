from app import db
from datetime import datetime
#dt_datetime = datetime.datetime.fromtimestamp(dt_value)
class Weather(db.Model):
    __tablename__ = "weather"
    id = db.Column(db.Integer, primary_key=True)
    main = db.Column(db.String(50))
    temp = db.Column(db.Float)
    feels_like = db.Column(db.Float)
    dt = db.Column(db.DateTime, default=datetime.utcnow)
    city = db.Column(db.String(50))

    def __repr__(self):
        return f'<Weather {self.main}>'
