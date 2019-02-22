# fetch the data from JCD

import requests

# the host address of JCD
hostname = 'https://api.jcdecaux.com/vls/v1/'

# the api key
api_key = '92be62130be380ad2925b05fc3b1e5b3ef1a5a55'


# get the list of stations from JCD
# the data return from this function is
# an array of json which has format like this.
# {
#   "number": 123,
#   "contract_name" : "Lyon",
#   "name": "stations name",
#   "address": "address of the station",
#   "position": {
#     "lat": 45.774204,
#     "lng": 4.867512
#   },
#   "banking": true,
#   "bonus": false,
#   "status": "OPEN",
#   "bike_stands": 20,
#   "available_bike_stands": 15,
#   "available_bikes": 5,
#   "last_update": <timestamp>
# }
# Usage:
#           stations = get_stations()   #return a list of stations
#           for station in stations:    # iterate each station in the station ist
#               station.id()            # get the id of a station
#               station.name()          # get the name of a station
def get_stations():
    # get the full url of the request
    req = hostname + 'stations' + '?apiKey=' + api_key
    data = requests.get(req).json()

    return data


# this function return an array of json data which has format
# like this
# {
#   "name" : "Lyon",
#   "commercial_name" : "Vélo'v",
#   "country_code" : "FR",
#   "cities" : [
#     "Lyon",
#     "Villeurbanne",
#   ]
# }
# Usage:
#               contracts = get_contracts()     # return a list of contracts
#               for contract in contracts:      # iterate each contract in the contracts
#                   contract.name()             # get the name of a contract
#                   contract.country_code()     # get the country code of a contract
def get_contracts():
    # ge the full url of the request
    req = hostname + 'contracts' + "?apiKey=" + api_key
    data = requests.get(req).json()

    return data