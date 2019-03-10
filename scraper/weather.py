from os import environ
from records import Database

import json
import re
import requests
import logging

from .log import logger

class Weather:
    def __init__(self):
        self.__host = environ['WEATHER_HOST']
        self.__key = environ['WEATHER_KEY']
        self.__db_host = environ['DB_HOST']
        self.__db_port = environ['DB_PORT']
        self.__db_user = environ['DB_USER']
        self.__db_passwd = environ['DB_PASSWD']
        self.__db_schema = environ['DB_SCHEMA']
        self.__db_name = environ['DB_NAME']
        self.__db_url = "{name}://{user}:{passwd}@{host}:{port}/{schema}".format(
            name=self.__db_name,
            user=self.__db_user,
            passwd=self.__db_passwd,
            host=self.__db_host,
            port=self.__db_port,
            schema=self.__db_schema)
        self.__db_conn = Database(self.__db_url)

        logger()

        logging.info('Established database connection')

    def current(self):
        try:
            req = requests.get('{host}/weather?q=dublin&APPID={key}'.format(
            host=self.__host, key=self.__key))
        except ConnectionError:
            logging.error('Connection error')

        if req.status_code != 200:
            return None

        return req.json()

    def forecast(self):
        try:
            req = requests.get('{host}/forecast?q=dublin&APPID={key}'.format(host=self.__host, key=self.__key))
        except ConnectionError:
            logging.error('Connection error')

        if req.status_code != 200:
            logging.warning(f'Bad request: {req.status_code}')         
            return None

        return req.json()

    def save_all(self):
        data = json.loads(json.dumps(self.forecast()))
        sql = open('scraper/sql/INSERT_FORECAST.sql').read()
        sql = re.sub(r'\s+', r' ', sql)
        
        if data != None and data.get('list', None) != None:
            for w_data in data['list']:
                for w in w_data['weather']:
                    insert_query = sql.format(
                        table='weather',
                        base=data.get('base', ''),
                        city_coord_lat=data['city']['coord']['lat'],
                        city_coord_lon=data['city']['coord']['lon'],
                        city_country=data['city']['country'],
                        city_id=data['city']['id'],
                        city_name=data['city']['name'],
                        city_population=data['city']['population'],
                        clouds_all='NULL' if w_data.get('clouds', 'NULL') == None
                        or w['main'] != 'Cloud' else data['clouds']['all'],
                        cnt=data['cnt'],
                        cod=data['cod'],
                        dt=w_data['dt'],
                        dt_text=w_data.get('dt_txt', '1970-01-01'),
                        main_grnd_level=w_data['main']['grnd_level'],
                        main_humidity=w_data['main']['humidity'],
                        main_pressure=w_data['main']['pressure'],
                        main_sea_level=w_data['main']['sea_level'],
                        main_temp=w_data['main']['temp'],
                        main_temp_kf=w_data['main']['temp_kf'],
                        main_temp_max=w_data['main']['temp_max'],
                        main_temp_min=w_data['main']['temp_min'],
                        sys_country=w_data['sys'].get('country', ''),
                        sys_id=w_data['sys'].get('id', 'NULL'),
                        sys_message=w_data['sys'].get('message', 'NULL'),
                        sys_pod=w_data['sys'].get('pod', 'NULL'),
                        sys_sunrise=w_data['sys'].get('sunrise', 'NULL'),
                        sys_sunset=w_data['sys'].get('sunset', 'NULL'),
                        sys_type=w_data['sys'].get('type', 'NULL'),
                        weather_desc='-'.join(w['description'].split(' ')),
                        weather_icon=w['icon'],
                        weather_id=w['id'],
                        weather_main=w['main'],
                        wind_deg=w_data['wind']['deg'],
                        wind_speed=w_data['wind']['speed'],
                        rain_1h='NULL' if w_data.get('rain', None) == None
                        or w['main'] != 'Rain' else w_data['rain'].get('1h', 'NULL'),
                        rain_3h='NULL' if w_data.get('rain', None) == None
                        or w['main'] != 'Rain' else w_data['rain'].get('3h', 'NULL'),
                        snow_1h='NULL' if w_data.get('snow', None) == None
                        or w['main'] != 'Snow' else w_data['snow'].get('1h', 'NULL'),
                        snow_3h='NULL' if w_data.get('snow', None) == None
                        or w['main'] != 'Snow' else w_data['snow'].get('3h', 'NULL'))

                    logging.info(f'{insert_query}')

                    self.__db_conn.bulk_query(insert_query)
