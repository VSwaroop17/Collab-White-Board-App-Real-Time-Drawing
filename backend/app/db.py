import pymongo

client = None
def connect_db():
    global client
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    return client

def get_whiteboard_collection():
    db = client["whiteboard_db"]
    return db["whiteboards"]