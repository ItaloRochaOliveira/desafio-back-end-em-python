from ..models.appointment_model import Appointment_model
from ..business.Professional_business import get_professional_by_id
from ..database.appointment_database import (
    get_appointment_by_id,
    get_appointment_by_id_professional,
    table_appointment,
)
from src.service.Gerator_id import Gerator_id
from datetime import datetime


class Appointment_business:
    def __init__(self):
        self.get_professional_by_id = get_professional_by_id
        self.get_appointment_by_id = get_appointment_by_id
        self.get_appointment_by_id_professional = get_appointment_by_id_professional
        self.table_appointment = table_appointment
        self.gerator_id = Gerator_id

    def get_appointments(self, id):
        appointments = self.get_appointment_by_id_professional(id)

        professional_exist = self.get_professional_by_id(id)

        if not professional_exist:
            raise FileNotFoundError("Professional don`t exist")

        if not appointments:
            raise FileNotFoundError("Professional don`t have appointments")

        if appointments:
            return appointments

    def set_appoitment(self, content):
        if type(content["professional_id"]) is not str:
            raise ValueError("Date have to be String")
        if content["professional_id"] == "":
            raise ValueError("Date have to be minimun 1 string")

        if type(content["date"]) is not str:
            raise ValueError("Date have to be String")
        if content["date"] == "":
            raise ValueError("Date have to be minimun 1 string")
        if (len(content["date"])) != 10:
            raise ValueError("date has to have this format: 00/00/0000")

        id = self.gerator_id.gerate_uuid4()
        created_at = datetime.now()

        newAppointment = Appointment_model(
            str(id), content["professional_id"], content["date"], created_at, ""
        )

        if content["professional_id"].count("id-mock"):
            self.table_appointment.insert(2, newAppointment.get_all_itens())
        else:
            self.table_appointment.insert(newAppointment.get_all_itens())

        return newAppointment.get_all_itens()

    def update_appointments(self, id, date):
        if type(date["date"]) is not str:
            raise ValueError("Date have to be String")
        if date["date"] == "":
            raise ValueError("Date have to be minimun 1 string")
        if (len(date["date"])) != 10:
            raise ValueError("date has to have this format: 00/00/0000")

        updated_at = datetime.now()

        appointment = self.get_appointment_by_id(id)

        if appointment == None:
            raise FileNotFoundError("Appointment don`t exist for update")

        content = Appointment_model(
            appointment["id"],
            appointment["professional_id"],
            date["date"],
            appointment["created_at"],
            updated_at,
        )

        if id.count("id-mock-appointment"):
            for appointment in self.table_appointment:
                if appointment["id"] == id:
                    self.table_appointment.remove(appointment)

            self.table_appointment.append(content.get_all_itens())
        else:
            self.table_appointment.update(content.get_all_itens(), ["id"])

        appointment_updated = self.get_appointment_by_id(id)

        return appointment_updated

    def delete_appointment(self, id):
        appointment = self.get_appointment_by_id(id)

        if appointment == None:
            raise FileNotFoundError(
                "Appointment don`t exist for exclusion or already deleted."
            )

        if id.count("id-mock-appointment"):
            for appointment in self.table_appointment:
                if appointment["id"] == id:
                    self.table_appointment.remove(appointment)
        else:
            self.table_appointment.delete(id=id)

        return "Appointment deleted successfully"
