import dataset

db = dataset.connect("sqlite:///db/createDatabase.db")


table_appointment = [
    {
        "id": "id-mock-appointment-1",
        "professional_id": "id-mock-1",
        "date": "21/07/2023",
        "created_at": "2023-06-16 11:16:17",
        "updated_at": "",
    },
    {
        "id": "id-mock-appointment-2",
        "professional_id": "id-mock-1",
        "date": "04/02/2024",
        "created_at": "2023-06-17 20:22:05.293083",
        "updated_at": "",
    },
]


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
