from bson import ObjectId
from dotenv import dotenv_values
from fastapi import APIRouter
from pymongo import MongoClient

from type_codecs import codec_options

config = dotenv_values("produtos/.env")


class DatabaseConnection:
    def __init__(self):
        self.client = MongoClient(config["CONNECTION_STRING"], serverSelectionTimeoutMS=5000)
        self.db = self.client.get_database(config["DATABASE_NAME"])
        self.coll = self.db.get_collection(config["COLLECTION_NAME"], codec_options=codec_options)

mongo = DatabaseConnection()


db_router = APIRouter()

@db_router.on_event("shutdown")
def close_connection():
    mongo.client.close()
