from src.business.Appointmente_business import Appointment_business
from ..mocks.appointment_database_mock import (
    get_appointment_by_id,
    get_appointment_by_id_professional,
    table_appointment,
)
from ..mocks.professional_database_mock import get_professional_by_id_mock
from ..mocks.Gerator_id_mock import Gerator_id
import unittest


class DerivedClassBusiness(Appointment_business):
    def __init__(self):
        self.get_professional_by_id = get_professional_by_id_mock
        self.get_appointment_by_id = get_appointment_by_id
        self.get_appointment_by_id_professional = get_appointment_by_id_professional
        self.table_appointment = table_appointment
        self.gerator_id = Gerator_id


class TestClassBusiness(unittest.TestCase):
    def test_get_appointments(self):
        appointment_business_mock = DerivedClassBusiness()

        self.assertEqual(
            appointment_business_mock.get_appointments("id-mock-1"),
            [
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
            ],
        )

    def test_set_appointment(self):
        appointment_business_mock = DerivedClassBusiness()
        content = {
            "professional_id": "id-mock-1",
            "date": "04/02/2024",
        }

        data = appointment_business_mock.set_appoitment(content)

        self.assertEqual(
            data,
            {
                "id": "new-id-mock",
                "professional_id": "id-mock-1",
                "date": "04/02/2024",
                "created_at": data["created_at"],
                "updated_at": "",
            },
        )

    def test_update_appointment(self):
        appointment_business_mock = DerivedClassBusiness()

        date = {"date": "31/05/2023"}

        data = appointment_business_mock.update_appointments(
            "id-mock-appointment-1", date
        )

        self.assertEqual(
            data,
            {
                "id": "id-mock-appointment-1",
                "professional_id": "id-mock-1",
                "date": "31/05/2023",
                "created_at": data["created_at"],
                "updated_at": data["updated_at"],
            },
        )

    # def test_delete_appointment(self):
    #     appointment_business_mock = DerivedClassBusiness()

    #     self.assertEqual(
    #         appointment_business_mock.delete_appointment("id-mock-appointment-1"),
    #         "Appointment deleted successfully",
    #     )


if __name__ == "__main__":
    unittest.main()
