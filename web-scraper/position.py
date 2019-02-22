# Create a position class
class Positon:

    # Initializer/Instance Attributes
    def __init__(self, lat, lng):
        self.__lat = lat
        self.__lng = lng

        # Function that to get the latitude and longtitude of the postion
        @property
        def lat(self):
            return self.__lat

        @property
        def lng(self):
            return self.__lng
