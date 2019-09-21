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
    def db_object(self):
        print("Select")

class Mysqlcore(object):
    def select(self):
        print("select")