import requests
import re
import logging

from os import environ
from records import Database
from json import dumps
from json import loads

from .log import logger


class Bike:
    def __init__(self):
        self.__host = environ['BIKE_HOST']
        self.__key = environ['BIKE_KEY']
        self.__db_host = environ['DB_HOST']
        self.__db_port = environ['DB_PORT']
        self.__db_user = environ['DB_USER']
        self.__db_passwd = environ['DB_PASSWD']
        self.__db_schema = environ['DB_SCHEMA']
        self.__db_name = environ['DB_NAME']
        self.__contracts_url = "{host}/contracts?apiKey={key}".format(
            host=self.__host, key=self.__key)
        self.__stations_url = "{host}/stations?apiKey={key}".format(
            host=self.__host, key=self.__key)
        self.__db_url = "{name}://{user}:{passwd}@{host}:{port}/{schema}".format(
            name=self.__db_name,
            user=self.__db_user,
            passwd=self.__db_passwd,
            host=self.__db_host,
            port=self.__db_port,
            schema=self.__db_schema)
        self.__db_conn = Database(self.__db_url)

        logger()

        logging.info(f'Established a connection to remote database')
        logging.info(f'Database address: {self.__db_host}')
        logging.info(f'Database port: {self.__db_port}')
        logging.info(f'Database name: {self.__db_schema}')

    def save_stations(self):
        try:
            req = requests.get(self.__stations_url)
        except ConnectionError:
            logging.error('Connection error')

        if req.status_code != 200:
            logging.warning(f'Fetched data from JCD database')
            logging.warning(f'Status code: {req.status_code}')
            return None

        logging.info(f'Fetched data from JCD database')

        data = loads(dumps(req.json()))

        insert_sql = open('scraper/sql/INSERT_STATION.sql').read()
        insert_sql = re.sub(r'\s+', r' ', insert_sql)

        logging.info(f'Load SQL file')

        query = ''

        for station in data:
            insert_query = insert_sql.format(
                id=station['number'],
                contract_name=re.sub(r"'+", r'', station['contract_name']),
                name=re.sub(r"'+", r'', station['name']),
                pos_lat=station['position']['lat'],
                pos_lon=station['position']['lng'],
                banking=station['banking'],
                bonus=station['banking'],
                bike_stands=station['bike_stands'],
                available_bike_stands=station['available_bike_stands'],
                available_bikes=station['available_bikes'],
                status=station['status'],
                last_update=station['last_update'],
                address=re.sub(r"'+", r'', station['address']))

            logging.info(f'Parse JSON data')
            logging.info(f'The SQL query: {insert_query}')

            query += insert_query

        self.__db_conn.bulk_query(query)

    def save_contracts(self):
        try:
            req = requests.get(self.__contracts_url)
        except ConnectionError:
            logging.error('Connection error')

        if req.status_code != 200:
            logging.warning(f'Fetched data from JCD database')
            logging.warning(f'Status code: {req.status_code}')
            return None

        logging.info(f'Fetched data from JCD database')

        data = loads(dumps(req.json()))
        sql = open('scraper/sql/INSERT_CONTRACT.sql').read()
        sql = re.sub(r'\s+', r' ', sql)

        logging.info(f'Load SQL file')

        query = ''

        for cont in data:
            if cont.get('cities', None) != None:
                for city in cont['cities']:
                    insert_query = sql.format(
                        name=cont['name'],
                        commerical_name=cont.get('commerical_name', 'NULL'),
                        country_code=cont['country_code'],
                        city=re.sub(r"'+", r'', city))

                    logging.info(f'Parse JSON data')
                    logging.info(f'The SQL query: {insert_query}')

                    query += insert_query
        self.__db_conn.bulk_query(query)