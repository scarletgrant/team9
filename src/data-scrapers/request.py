# Fetches the retreived bike- and weather data from our server to provide this data to the client

from .bike import Bike
from .weather import Weather

if __name__ == '__main__':
    bike = Bike()
    weather = Weather()

    bike.save_stations()
    bike.save_contracts()
    weather.save_all()
