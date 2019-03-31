# Old version, Placeholder for script to start the application all at once

export WEATHER_HOST='http://api.openweathermap.org/data/2.5'
export WEATHER_KEY='dd0a4798e371d086cfa6a26a7b45743c'
export DB_USER='postgres'
export DB_PASSWD='UCDTeam9'
export DB_PORT='5432'
export DB_HOST='188.166.168.147'
export DB_SCHEMA='postgres'
export DB_NAME='postgres'
export BIKE_HOST='https://api.jcdecaux.com/vls/v1'
export BIKE_KEY='92be62130be380ad2925b05fc3b1e5b3ef1a5a55'

python3 -m scraper.request
