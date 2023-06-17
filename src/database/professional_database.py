import dataset

db = dataset.connect("sqlite:///db/createDatabase.db")

table_professional = db["professional"]


def get_professional_by_id(id):
    for appointment in table_professional:
        if appointment["id"] == id:
            return appointment
