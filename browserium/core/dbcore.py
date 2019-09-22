# Author: @Corefinder
# Language: Python
# Copyrights: SoumyajitBasu
# Purpose: The purpose of the class DBcore is to have all the db query configurations
# can be used across all db related functionalities for Postgres and Mysql

from utility import Utility

class DBcore(object):
    def __init__(self):
        self.ut = Utility()
        self.psql = self.postgrescore()
        self.mysql = self.mysqlcore()

class Postgrescore(object):
    # configure postgres to create cursor object
    def create_cursor_object(self, username, password, hostname, port=5432, databasename):
        try:
            # Create postgres connection object
            connection = psycopg2.connect(
                user=username,
                password=password,
                host=host,
                port=port,
                database=databasename
            )
            # Create postgres cursor object
            cursor = connection.cursor()
            return cursor
        except(Exception, psycopg2.Error) as error:
            self.log.log_error(error)

    def execute_query_object(self, cursor_obj, query, query_condition="fetchAll"):
        # Define cursor object
        cursor = cursor_obj
        # Execute respective query
        cursor.execute(query)
        # Fetch all data
        query_data = None
        ldata = []
        if query_condition == 'fetchAll':
            query_data = cursor_obj.fetchall()
            for row in query_data:
                ldata.append(row)
        if query_condition == 'fetchOne':
            query_data = cursor_obj.fetchone()
            ldata.append(query_data)
        if query_condition == 'fetchMany':
            query_data = cursor_obj.fetchmany(size)
            ldata.append(query_data)
        return ldata

class Mysqlcore(object):
    # Configure mysql to create cursor object
    def cursor_mysql(self, username, password, hostname, port, databasename):
        try:
            # Create mysql connection object
            connection = mysql.connector.connect(
                user=username,
                password=password,
                host=host,
                port=port,
                database=databasename
            )
            # Create mysql cursor object
            cur = connection.cursor()
            return cursor
        except(Exception, mysql.error) as error:
            self.log.log_error(error)

    def execute_query_object(self, cursor_obj, query):