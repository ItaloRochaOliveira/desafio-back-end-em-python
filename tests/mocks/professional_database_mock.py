import dataset

db = dataset.connect("sqlite:///db/createDatabase.db")

table_professional = [
    {
        "id": "id-mock-1",
        "nome": "name-mock-1",
        "nome_social": "",
        "created_at": "Sat, 17 Jun 2023 20:22:57 GMT",
        "updated_at": "",
    },
    {
        "id": "id-mock-2",
        "nome": "name-mock-2",
        "nome_social": "",
        "created_at": "Sat, 17 Jun 2023 20:22:57 GMT",
        "updated_at": "",
    },
]


def get_professional_by_id_mock(id):
    for appointment in table_professional:
        if appointment["id"] == id:
            return appointment
