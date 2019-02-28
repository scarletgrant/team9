""" The Contract Class

creating this contract class is to store the data that we
retrieve from the JCDecaux developer
Contract class is the data about which
company that provide the bike for the
station
"""


# Create a contract class
class Contract:
    """ The Contract represents a real contract company.
    
        Each station should have a bike provider for that 
        station. So that contract company could be represented 
        by this class.

    Attributes:
        name:   the name of a comtract, usually it used to identify 
                a contract.
        commerical_name: The real name of a contract. It is the well
                            known name for that contract in the industry
        country_code: a code used to identify a country.
        cities: a list of cities. The contract has services in these cities.
     """

    # Initializer/Instance Attributes
    def __init__(self, name='', cname='', country_code='', cities=''):
        """ Create a new instance of this class """
        self.__name = name
        self.__commercial_name = cname
        self.__country_code = country_code
        # this empty list is to store the cities
        self.__cities = cities

    # Function to get the contract name
    @property
    def name(self):
        """ The unique identifier for a contract """
        return self.__name

    # Function to get commercial_name
    @property
    def commercial_name(self):
        """ The well known name for a contract """
        return self.__commercial_name

    # Function to get country_code
    @property
    def country_code(self):
        """ The country a contract belongs to """
        return self.__country_code

    # Function to get cities
    @property
    def cities(self):
        """ Cities where a contract has related services in there """
        return self.__cities
