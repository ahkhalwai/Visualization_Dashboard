from flask import Flask, render_template, jsonify, request
from model import db, Insight, setup_db
import json
import psycopg2


app = Flask(__name__)
setup_db(app)

''' 
load json to db 
'''

with app.app_context():
    db.drop_all()
    db.create_all()

# load json file
with open('jsondata.json') as f:
    data = json.load(f)

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    database="vd",
    user="postgres",
    password="8089"
)

# Create a cursor
cur = conn.cursor()

# Create a table
cur.execute("""
    CREATE TABLE IF NOT EXISTS insight (
        id SERIAL PRIMARY KEY,
        end_year TEXT,
        intensity INTEGER,
        sector TEXT,
        topic TEXT,
        insight TEXT,
        url TEXT,
        region TEXT,
        start_year TEXT,
        impact TEXT,
        added TEXT,
        published TEXT,
        country TEXT,
        relevance INTEGER,
        pestle TEXT,
        source TEXT,
        title TEXT,
        likelihood INTEGER
    )
""")   

# Insert the data into the table
for item in data:
    end_year = item.get('end_year') or None
    intensity = item.get('intensity') or None
    relevance = item.get('relevance') or None
    likelihood = item.get('likelihood') or None

    cur.execute("""
        INSERT INTO insight (
            end_year,
            intensity,
            sector,
            topic,
            insight,
            url,
            region,
            start_year,
            impact,
            added,
            published,
            country,
            relevance,
            pestle,
            source,
            title,
            likelihood
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        end_year,
        intensity,
        item.get('sector'),
        item.get('topic'),
        item.get('insight'),
        item.get('url'),
        item.get('region'),
        item.get('start_year'),
        item.get('impact'),
        item.get('added'),
        item.get('published'),
        item.get('country'),
        relevance,
        item.get('pestle'),
        item.get('source'),
        item.get('title'),
        likelihood
    ))

# Commit the changes
conn.commit()

# Close the connection
cur.close()
conn.close() 

'''
Page Get Data and Index.html
'''    

@app.route('/')
def index():
    return render_template('index.html')


'''
Add end year filter in the dashboard
Add topics filters in the dashboard
Add sector filter in the dashboard
Add region filter in the dashboard
Add PEST filter in the dashboard
Add Source filter in the dashboard
Country
Any other control or filters that you can add from the data, best of your knowledge 


The dashboard should read the data from the database.
Create API in Python to get data from the database

'''


@app.route('/data', methods=['GET'])
def get_data():
    filters = request.args
    query = Insight.query

    if 'sector' in filters and filters['sector']:
        query = query.filter(Insight.sector == filters['sector'])
    if 'country' in filters and filters['country']:
        query = query.filter(Insight.country == filters['country'])
    if 'topic' in filters and filters['topic']:
        query = query.filter(Insight.topic == filters['topic'])
    if 'region' in filters and filters['region']:
        query = query.filter(Insight.region == filters['region'])
    if 'pestle' in filters and filters['pestle']:
        query = query.filter(Insight.pestle == filters['pestle'])
    if 'source' in filters and filters['source']:
        query = query.filter(Insight.source == filters['source'])
    if 'intensity' in filters and filters['intensity']:
        query = query.filter(Insight.intensity == filters['intensity'])                
    if 'likelihood' in filters and filters['likelihood']:
        query = query.filter(Insight.likelihood == filters['likelihood'])
    if 'relevance' in filters and filters['relevance']:
        query = query.filter(Insight.relevance == filters['relevance'])
    if 'end_year' in filters and filters['end_year']:
        query = query.filter(Insight.end_year == filters['end_year'])
    if 'start_year' in filters and filters['source']:
        query = query.filter(Insight.start_year == filters['start_year'])                   

    ins = query.all()
    result = []
    for insight in ins:
        insight_data = {
            'id': insight.id,
            'end_year': insight.end_year,
            'intensity': insight.intensity,
            'sector': insight.sector,
            'topic': insight.topic,
            'insight': insight.insight,
            'url': insight.url,
            'region': insight.region,
            'start_year': insight.start_year,
            'impact': insight.impact,
            'added': insight.added,
            'published': insight.published,
            'country': insight.country,
            'relevance': insight.relevance,
            'pestle': insight.pestle,
            'source': insight.source,
            'title': insight.title,
            'likelihood': insight.likelihood
        }
        result.append(insight_data)
    
    return jsonify(result) 

if __name__ == '__main__':
    app.run(debug=True)
