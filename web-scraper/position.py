"""
creating this Position class is to store the data that we
retrieve from the JCDecaux developer
Position class is the data about each bike station postion
"""


# Create a Position class
class Positon:

    # Initializer/Instance Attributes
    def __init__(self, lat, lng):
        self.__lat = lat
        self.__lng = lng

        # Function to get the latitude of position
        @property
        def lat(self):
            return self.__lat

        # Function to get longtitude of the postion
        @property
        def lng(self):
            return self.__lng
