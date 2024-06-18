## CLI change to folder location
```
cd /Users/user/Visualization_Dashboard
```
## Setup Environment
```
python3 -m venv env
source env/bin/activate
```
## Install Required
```
Try:

pip3 install -r requirements.txt

Else: 

python3 -m pip install -r requirements.txt

```
## Any update in CLF run this command after install
```
pip3 freeze > requirements.txt
```
## Run Flask
```
export FLASK_APP=app.py;
export FLASK_ENV=development # enables debug mode
flask run --reload
```

## Output

![Filter 1](images/1.png)
![Filter 2](images/2.png)


## API Reference


### Endpoints 

#### GET /data

- get the data.
- Returns: whole data.
- Sample: `curl -X GET http://127.0.0.1:5000/data`
```
[{
    "added": "July, 03 2016 05:28:48", 
    "country": "", 
    "end_year": null, 
    "id": 1000, 
    "impact": "", 
    "insight": "Greenhouse gas", 
    "intensity": 2, 
    "likelihood": 2, 
    "pestle": "", 
    "published": "July, 03 2016 00:00:00", 
    "region": "World", 
    "relevance": 1, 
    "sector": "", 
    "source": "Wikipedia", 
    "start_year": "", 
    "title": "Earth's surface temperature could exceed historical values as early as 2047.", 
    "topic": "", 
    "url": "https://en.wikipedia.org/wiki/Greenhouse_gas"
  }]
```
#### GET /data Filter Intensity

- get the data of intensity.
- Returns: intensity data.
- Sample: `curl -X GET "http://127.0.0.1:5000/data?intensity=6"`
```
[{
    "added": "July, 07 2016 02:27:51", 
    "country": "", 
    "end_year": null, 
    "id": 980, 
    "impact": "", 
    "insight": "McKinsey: Cars, petrochemicals in oil-market 'tug of war'", 
    "intensity": 6, 
    "likelihood": 3, 
    "pestle": "Industries", 
    "published": "June, 07 2016 00:00:00", 
    "region": "Europe", 
    "relevance": 2, 
    "sector": "Energy", 
    "source": "Oil and Gas Journal", 
    "start_year": "", 
    "title": "Energy demand will grow in emerging and developing countries and decline in Europe and North America.", 
    "topic": "energy", 
    "url": "http://www.ogj.com/articles/2016/07/mckinsey-cars-petrochemicals-in-oil-market-tug-of-war.html"
  }]
```
#### GET /data Filter Country and Sector

- get the data of Country and Sector.
- Returns: Country and Sector data.
- Sample: `curl -X GET "http://127.0.0.1:5000/data?country=Mexico&sector=Environment"`
```
[{
    "added": "January, 20 2017 03:26:40", 
    "country": "Mexico", 
    "end_year": null, 
    "id": 4, 
    "impact": "", 
    "insight": "WRI Partnership Aims to Foster Supply Chain Transparency, Zero-Deforestation Strategies", 
    "intensity": 6, 
    "likelihood": 2, 
    "pestle": "Environmental", 
    "published": "January, 18 2017 00:00:00", 
    "region": "Central America", 
    "relevance": 3, 
    "sector": "Environment", 
    "source": "sustainablebrands.com", 
    "start_year": "", 
    "title": "Mars, Unilever, Cargill and Mondel\u0113z are already using GFW Commodities to assess deforestation risks in their palm oil, soy and cocoa supply chains across a collective area of land the size of Mexico.", 
    "topic": "oil", 
    "url": "http://www.sustainablebrands.com/news_and_views/supply_chain/sustainable_brands/wri_partnership_aims_foster_supply_chain_transparency"
  }]
```

