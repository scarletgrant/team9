import requests
""" 
This file contains only one function, the function return a json data read from JCD
 """
""" 
 @hostname: the host address of JCD
 @api_key: the api key
 @req: the full request which will be send from the client to JCD
"""

hostname = 'https://api.jcdecaux.com/vls/v1/'
api_key = '92be62130be380ad2925b05fc3b1e5b3ef1a5a55'
req = hostname + 'stations' + '?' + 'apiKey=' + api_key
"""
Fetch the data from JCD, and return the json data 
@Input: void
@Output: the json data
 """


def getData():
    return requests.get(req)
