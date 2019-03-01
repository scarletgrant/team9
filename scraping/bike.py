import requests
import re

from os import environ
from records import Database
from json import dumps
from json import loads


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

    def save_stations(self):
        req = requests.get(self.__stations_url)

        if req.status_code != 200:
            return None

        data = loads(dumps(req.json()))

        insert_sql = open('sql/INSERT_STATION.sql').read()
        insert_sql = re.sub(r'\s+', r' ', insert_sql)
        select_sql = open('sql/SELECT_STATIONS.sql').read()
        select_sql = re.sub(r'\s+', r' ', select_sql)

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

            query += insert_query

        self.__db_conn.bulk_query(query)

    def save_contracts(self):
        req = requests.get(self.__contracts_url)

        if req.status_code != 200:
            return None

        data = loads(dumps(req.json()))
        sql = open('sql/INSERT_CONTRACT.sql').read()
        sql = re.sub(r'\s+', r' ', sql)

        query = ''

        for cont in data:
            for city in cont['cities']:
                insert_query = sql.format(
                    name=cont['name'],
                    commerical_name=cont['commerical_name'],
                    country_code=cont['country_code'],
                    city=city)

                query += insert_query
            self.__db_conn.query(query)