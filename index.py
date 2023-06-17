from flask import Flask, jsonify, make_response, request
from models.appointment_model import Appointment_model
from datetime import datetime
import dataset
import uuid

app = Flask(__name__)
app.json.sort_keys = False

db = dataset.connect("sqlite:///db/createDatabase.db")

professional = [{"id": 1, "nome": "fernanda"}]

consultas = [{"id": 1, "nome": "Fernanda", "professional_id": 1, "data": "01/02/2024"}]

table_professional = db["professional"]
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


def gerate_uuid4():
    return uuid.uuid4()


@app.route("/appointment/<id>", methods=["GET"])
def get_consultas(id):
    appointments = get_appointment_by_id_professional(id)
    if appointments:
        return make_response(jsonify(appointments), 200)
    else:
        return make_response(jsonify("Professional don`t have appointments"), 404)


@app.route("/appointment", methods=["POST"])
def set_consultas():
    content = request.json

    id = gerate_uuid4()
    created_at = datetime.now()

    newAppointment = Appointment_model(
        str(id), content["professional_id"], content["date"], created_at, ""
    )

    table_appointment.insert(newAppointment.get_all_itens())

    return make_response(
        jsonify(
            message="Appointment created successfully",
            appointment=newAppointment.get_all_itens(),
        )
    )


@app.route("/appointment/<id>", methods=["PUT"])
def update_appointment(id):
    try:
        date = request.json

        updated_at = datetime.now()

        appointment = get_appointment_by_id(id)

        content = Appointment_model(
            appointment["id"],
            appointment["professional_id"],
            date["date"],
            appointment["created_at"],
            updated_at,
        )

        table_appointment.update(content.get_all_itens(), ["id"])

        appointment_updated = get_appointment_by_id(id)

        return make_response(
            jsonify(
                message="Appointment updated successfully",
                appointment=appointment_updated,
            )
        )
    except Exception as erro:
        return make_response(jsonify("erro"), 400)


app.run(debug=True)
