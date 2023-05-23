import configparser
from peewee import *

config = configparser.ConfigParser()
config.read('db.ini')

db = MySQLDatabase(
    host=config["database"]["host"],
    database=config["database"]["name"],
    user=config["database"]["user"],
    password=config["database"]["password"]
)
