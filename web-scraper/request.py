'''
REMEMBER: to remove the api key before publishing and store key in database

REQUEST.PY
The request.py fetches the data from JCDecaux. It gets the list of stations, 
the data returned from this function is an array in json format.

DATA FORMAT STATION DATA
Here is an example of the data that the station returns:
{
"number": 123,
"contract_name" : "Lyon",
"name": "stations name",
"address": "address of the station",
"position": {
   "lat": 45.774204,
   "lng": 4.867512
   },
   "banking": true,
   "bonus": false,
   "status": "OPEN",
   "bike_stands": 20,
   "available_bike_stands": 15,
   "available_bikes": 5,
   "last_update": <timestamp>
 }
 
Here is an example how we could use the functions to get the data:
           stations = get_stations()   # returns a list of stations
           for station in stations:    # iterates over each station in the station ist
               station['id]            # gets the id of a station
               station['name']         # gets the name of a station

DATA FORMAT CONTRACT DATA
The get_contracts function returns an array of json data which has format like below:
{
   "name" : "Lyon",
   "commercial_name" : "Vélo'v",
   "country_code" : "FR",
   "cities" : [
     "Lyon",
     "Villeurbanne",
   ]
 }
 Usage:
               contracts = get_contracts()         # return a list of contracts
               for contract in contracts:          # iterate each contract in the contracts
                   contract['name']                # get the name of a contract
                   contract['country_code']        # get the country code of a contract              
'''

# Import package to send HTTP/1.1 requests using Python. 
# With it, you can add content like headers, form data, multipart files, and parameters via simple Python libraries. 
# It also allows you to access the response data of Python in the same way.
import requests

# The host address of JCDecaux
hostname = 'https://api.jcdecaux.com/vls/v1/'

# The api key provided by JCDecaux
api_key = '92be62130be380ad2925b05fc3b1e5b3ef1a5a55'

# Function to get the list of stations from JCDecaux
def get_stations():
    # Gets the full url for the request
    req = hostname + 'stations' + '?apiKey=' + api_key
    data = requests.get(req).json()
    # returns data to the variables (to be defined)
    return data

# Function to get the list of contracts from JCDecaux
def get_contracts():
    # get the full url of the request
    req = hostname + 'contracts' + "?apiKey=" + api_key
    data = requests.get(req).json()
    return data
