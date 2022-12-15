from dotenv import dotenv_values
from fastapi import APIRouter
from pymongo import MongoClient

from type_codecs import codec_options

config = dotenv_values("produtos/.env")


class DatabaseConnection:
    def __init__(
            self,
            connection_string=config["CONNECTION_STRING"],
            database_name=config["DATABASE_NAME"],
            collection_name=config["COLLECTION_NAME"]):
        self.client = MongoClient(connection_string, serverSelectionTimeoutMS=5000)
        self.db = self.client.get_database(database_name)
        self.coll = self.db.get_collection(collection_name, codec_options=codec_options)

mongo = DatabaseConnection()


db_router = APIRouter()

@db_router.on_event("shutdown")
def close_connection():
    mongo.client.close()
