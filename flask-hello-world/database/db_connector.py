from pymongo import MongoClient

def get_db(mongo_uri):
    client = MongoClient(mongo_uri)
    db = client.get_default_database()
    return db