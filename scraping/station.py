"""
Author: Scarlet Grant
Copyright: © 2019 Team9

NOTE FOR TEAM: renamed 'id' (as defined in UML diagram) to 'station_number_in_contract'. JCDecaux notes that this number is not an id,
so we should consider to adjust that in our UML and create a new unique key in the database with number and contractname combined for example.

STATION.PY
The station class creates object instances of the class station to define the retreived data from JCDeacaux regarding their stations.

@parameters:

Document name conventions:  Data type:   Naming by JCDecaux:
Static data:
station_number_in_contract  integer       - number: number of the station. This is NOT an id, thus it is unique only inside a contract.
contract_name               string        - contract_name: name of the contract of the station
name                        string        - name: name of the station
address                     string        - address: address of the station. As it is raw data, sometimes it will be more of a comment than an address.
position                    position.py   - position: position of the station in WGS84 format -  attributes: lat,lng
banking                     boolean       - banking: indicates whether this station has a payment terminal
bonus                       boolean       - bonus: indicates whether this is a bonus station

Dynamic data:
status                      string        - status: indicates whether this station is CLOSED or OPEN
bike_stands                 integer       - bike_stands: the number of operational bike stands at this station
available_bike_stands       integer       - available_bike_stands: the number of available bike stands at this station
available_bikes             integer       - available_bikes: the number of available and operational bikes at this station
last_update                 string        - last_update: timestamp indicating the last update time in milliseconds since Epoch

"""


# This class creates an instance of a station class object
class Station:

    # Init function that initializes recurring station attributes
    def __init__(self, id, contract_name, name, address, position, banking,
                 bonus, status, bike_stands, available_bike_stands,
                 available_bikes, last_update):
        self.__id = id
        self.__contract_name = contract_name
        self.__name = name
        self.__address = address
        self.__position = position
        self.__banking = banking
        self.__status = status
        self.__bike_stands = bike_stands
        self.__available_bike_stands = available_bike_stands
        self.__available_bikes = available_bikes
        self.__last_update = last_update

    # Get's the id of the station (integer)
    @property
    def id(self):
        return self.__id

    # Get's the contract_name, which is the company that owns the station. (string)
    @property
    def contract_name(self):
        return self.__contract_name

    # Get's the name of the station. (string)
    @property
    def name(self):
        return self.__name

    # Get's the address of the station. (string)
    @property
    def address(self):
        return self.__address

    # Get's the position of the station in WGS84 format
    # (lat, lng: position.py class attributes)
    @property
    def position(self):
        return self.__position

    # Get's the presence of a payment terminal at the station (boolean)
    @property
    def banking(self):
        return self.__banking

    # Get's the status (String: OPEN, CLOSED) of the station.
    @property
    def status(self):
        return self.__status

    # Get's the address (string) of the station.
    @property
    def bike_stands(self):
        return self.__bike_stands

    # Get's the number of available bike stands (integer) of the station.
    @property
    def available_bike_stands(self):
        return self.__available_bike_stands

    # Get's the number of available bikes (integer) station.
    @property
    def available_bikes(self):
        return self.__available_bikes

    # Get's the timestamp of the last update of the station (string).
    @property
    def last_update(self):
        return self.__last_update
