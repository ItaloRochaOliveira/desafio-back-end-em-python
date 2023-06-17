import dataset

db = dataset.connect("sqlite:///db/createDatabase.db")


table_appointment = db["appointment"]


def get_appointment_by_id_professional(id):
    appointments = []
    for appointment in table_appointment:
        if appointment["professional_id"] == id:
            appointments.append(appointment)

    return appointments


def get_appointment_by_id(id):
    for appointment in table_appointment:
        if appointment["id"] == id:
            return appointment
