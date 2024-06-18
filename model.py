import os
from sqlalchemy import String, Integer
from flask_sqlalchemy import SQLAlchemy
import json
from flask_migrate import Migrate


'''
Data
Json file: jsondata.json
Use given json data
Create a database (of your interest such as mongodb, postgresql, sql) from the Json data given.
Use Flask or Django framework to design and develop a dashboard for Back-end
'''

database_path = 'postgresql://postgres:8089@localhost:5432/vd'
db = SQLAlchemy()
migrate = Migrate(db)

def setup_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    Migrate(app, db)

class Insight(db.Model):
    __tablename__ = 'insight'

    id = db.Column(db.Integer, primary_key=True)
    end_year = db.Column(db.String)
    intensity = db.Column(db.Integer)
    sector = db.Column(db.String)
    topic = db.Column(db.String)
    insight = db.Column(db.String)
    url = db.Column(db.String)
    region = db.Column(db.String)
    start_year = db.Column(db.String)
    impact = db.Column(db.String)
    added = db.Column(db.String)
    published = db.Column(db.String)
    country = db.Column(db.String)
    relevance = db.Column(db.Integer)
    pestle = db.Column(db.String)
    source = db.Column(db.String)
    title = db.Column(db.String)
    likelihood = db.Column(db.Integer)

    def __init__(self, end_year, intensity, sector, topic, insight, url, region, start_year, impact, added, published, country, relevance, pestle, source, title, likelihood):
        self.end_year = end_year
        self.intensity = intensity
        self.sector = sector
        self.topic = topic
        self.url = url
        self.region = region
        self.start_year = start_year
        self.impact = impact
        self.added = added
        self.published = published
        self.country = country
        self.relevance = relevance
        self.pestle = pestle
        self.source = source
        self.title = title
        self.likelihood = likelihood

    def format(self):
        return {
          'id': self.id,
          'end_year': self.end_year,
          'intensity': self.intensity,
          'sector' : self.sector,
          'topic' : self.topic,
          'url' : self.url,
          'region' : self.region,
          'start_year' : self.start_year,
          'impact' : self.impact,
          'added' : self.added,
          'published' : self.published,
          'country' : self.country,
          'relevance' : self.relevance,
          'pestle' : self.pestle,
          'source' : self.source,
          'title' : self.title,
          'likelihood' : self.likelihood
          }