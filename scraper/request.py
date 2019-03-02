import asyncio

from .bike import Bike
from .weather import Weather
from time import sleep

if __name__ == '__main__':
    bike = Bike()
    weather = Weather()

    bike.save_stations()
    bike.save_contracts()
    weather.save_all()
