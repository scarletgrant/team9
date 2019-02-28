class Weather:
    def __init__(self):
        self.__coord = dict()
        self.__weather = []
        self.__base = ''
        self.__main = dict()
        self.__visibility = 0
        self.__wind = dict()
        self.__clouds = dict()
        self.__dt = 0
        self.__sys = dict()
        self.__id = 0
        self.__name = ''
        self.__cod = 0

    @property
    def coord(self):
        return self.__coord

    @coord.setter
    def coord(self, lat, lon):
        self.__coord['lon'] = lon
        self.__coord['lat'] = lat

    @property
    def weather(self):
        return self.__weather

    @weather.setter
    def weather(self, id=0, main='', desc='', icon=''):
        self.__weather['id'] = id
        self.__weather['main'] = main
        self.__weather['desc'] = desc
        self.__weather['icon'] = icon

    @property
    def base(self):
        return self.__base

    @base.setter
    def base(self, base=''):
        self.__base = base

    @property
    def main(self):
        return self.__main

    @main.setter
    def main(self,
             temp=0.0,
             pressure=0.0,
             humidity=0.0,
             temp_min=0.0,
             temp_max=0.0):
        self.__main['temp'] = temp
        self.__main['pressure'] = pressure
        self.__main['humidity'] = humidity
        self.__main['temp_min'] = temp_min
        self.__main['temp_max'] = temp_max

    @property
    def visibility(self):
        return self.__visibility

    @visibility.setter
    def visibility(self, vis=0):
        self.__visibility = vis

    @property
    def wind(self):
        return self.__wind

    @wind.setter
    def wind(self, speed=0.0):
        self.__wind['speed'] = speed

    @property
    def clouds(self):
        return self.__clouds

    @clouds.setter
    def clouds(self, all=0):
        self.__clouds['all'] = all

    @property
    def dt(self):
        return self.__dt

    @dt.setter
    def dt(self, dt=0):
        self.__dt = dt

    @property
    def sys(self):
        return self.__sys

    @sys.setter
    def sys(self, type=0, id=0, message=0.0, country='', sunrise=0, sunset=0):
        self.__sys['type'] = type
        self.__sys['id'] = id
        self.__sys['message'] = message
        self.__sys['country'] = country
        self.__sys['sunrise'] = sunrise
        self.__sys['sunset'] = sunset

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id=0):
        self.__id = id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name=''):
        self.__name = name

    @property
    def cod(self):
        return self.__cod

    @cod.setter
    def cod(self, cod=0):
        self.__cod = cod