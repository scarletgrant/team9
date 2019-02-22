# Create a contract class
class Contract:

    # Initializer/Instance Attributes
    def __init__(self, name, commercial_name, country_code, cities):
        self.__name = name
        self.__commercial_name = commercial_name
        self.__country_code = country_code
        self.__cities = []

    @property
    def name(self):
        return self.__name

    @property
    def commercial_name(self):
        return self.__commercial_name

    @property
    def country_code(self):
        return self.__country_code

    @property
    def cities(self):
        return self.__cities
