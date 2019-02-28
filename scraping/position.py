""" The Position Class

creating this Position class is to store the data that we
retrieve from the JCDecaux developer
Position class is the data about each bike station postion
"""


# Create a Position class
class Positon:
    """ The Position represents a location in the map.
    
    Attributes:
        lat: the latitude
        lng: the longitude
     """

    # Initializer/Instance Attributes
    def __init__(self, lat=0.0, lng=0.0):
        self.__lat = lat
        self.__lng = lng

    # Function to get the latitude of position
    @property
    def lat(self):
        """ The latitude """
        return self.__lat

    # Function to get longtitude of the postion
    @property
    def lng(self):
        """ The longitude """
        return self.__lng
