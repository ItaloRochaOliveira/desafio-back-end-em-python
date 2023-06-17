from datetime import datetime
import dataset
import uuid

db = dataset.connect("sqlite:///db/createDatabase.db")

table_professional = db["professional"]


def get_professional_by_id(id):
    for appointment in table_professional:
        if appointment["id"] == id:
            return appointment


def gerate_uuid4():
    return uuid.uuid4()
