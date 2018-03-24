from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import PrimaryKeyConstraint
from sqlalchemy import Column, Integer, Unicode, DateTime, Numeric

app = Flask(__name__)
# import pdb; pdb.set_trace()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://gaurav:gaurav28@localhost/gaurav'
db = SQLAlchemy(app)


class Location(db.Model):
    __tablename__ = 'location'
    id = Column('id', Integer)
    description = Column('description', Unicode)
    datetime = Column('datetime', DateTime)
    longitude = Column('longitude', Numeric)
    latitude = Column('latitude', Numeric)
    elevation = Column('elevation', Integer)
    __table_args__ = (
        PrimaryKeyConstraint('id', 'description', 'datetime'),
        {},
    )

    def __init__(self, id, description, datetime, longitude, latitude, elevation):
        self.id = id
        self.description = description
        self.datetime = datetime
        self.longitude = longitude
        self.latitude = latitude
        self.elevation = elevation