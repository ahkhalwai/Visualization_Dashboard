## CMD change to folder location

cd /Users/musef/Udacity/Visualization_Dashboard

## Setup Environment

python3 -m venv env
source env/bin/activate

## Install Required

pip3 install -r requirements.txt

pip3 install Flask Flask-SQLAlchemy
pip3 install pandas
pip3 install psycopg2-binary

pip3 freeze > requirements.txt

## Run Flask

export FLASK_APP=app.py;
export FLASK_ENV=development # enables debug mode
flask run --reload