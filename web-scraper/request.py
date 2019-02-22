import requests
""" 
This file contains only one function, the function return a json data read from JCD
 """
""" 
 @hostname: the host address of JCD
 @api_key: the api key
"""

hostname = 'https://api.jcdecaux.com/vls/v1/'
api_key = '92be62130be380ad2925b05fc3b1e5b3ef1a5a55'


def get_stations():
    req = hostname + 'stations' + '?apiKey=' + api_key
    data = requests.get(req).json()

    return data


def get_contracts():
    req = hostname + 'contracts' + "?apiKey=" + api_key
    data = requests.get(req).json()

    return data
