import pymongo
from config import Config

from dataclasses import dataclass


@dataclass
class Collection:
    USERS = "users"


class Database:
    client = pymongo.MongoClient(Config.DATABASE_URL)
    database = client[Config.DATABASE_NAME]

    def save(self, obj):
        collection = obj.collection
        self.database[collection].insert_one(dict(obj))


database = Database()
