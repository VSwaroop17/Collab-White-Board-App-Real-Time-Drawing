from .db import get_whiteboard_collection

def save_canvas_state(room_id, canvas_data):
    collection = get_whiteboard_collection()
    collection.update_one(
        {"room_id": room_id},
        {"$set": {"canvas_data": canvas_data}},
        upsert=True
    )

def load_canvas_state(room_id):
    collection = get_whiteboard_collection()
    doc = collection.find_one({"room_id": room_id})
    return doc["canvas_data"] if doc else None