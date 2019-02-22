"""
creating this contract class is to store the data that we
retrieve from the JCDecaux developer
Contract class is the data about which
company that provide the bike for the
station
"""


# Create a contract class
class Contract:

    # Initializer/Instance Attributes
    def __init__(self, name, commercial_name, country_code, cities):
        self.__name = name
        self.__commercial_name = commercial_name
        self.__country_code = country_code
        # this empty list is to store the cities
        self.__cities = []

    # Function that get the contract name
    @property
    def name(self):
        return self.__name

    # Function that get commercial_name
    @property
    def commercial_name(self):
        return self.__commercial_name

    @property
    def country_code(self):
        return self.__country_code

    @property
    def cities(self):
        return self.__cities
