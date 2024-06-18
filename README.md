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

