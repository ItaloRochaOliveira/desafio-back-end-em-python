from flask import Flask, jsonify, make_response, request
from src.business.Appointmente_business import Appointment_business

app = Flask(__name__)
app.json.sort_keys = False


@app.route("/appointment/<id>", methods=["GET", "PUT", "DELETE"])
def api_appointment_id(id):
    try:
        if request.method == "GET":
            return make_response(jsonify(Appointment_business.get_appointments(id)))
        elif request.method == "PUT":
            date = request.json
            return make_response(
                jsonify(
                    message="Appointment updated successfully",
                    appointment=Appointment_business.update_appointments(id, date),
                )
            )
        elif request.method == "DELETE":
            return make_response(
                jsonify(message=Appointment_business.delete_appointment(id))
            )
    except ValueError as erro:
        return make_response(jsonify(str(erro)), 400)
    except FileNotFoundError as erro:
        return make_response(jsonify(str(erro)), 404)
    except Exception as erro:
        return make_response(jsonify(str(erro)), 500)


@app.route("/appointment", methods=["POST"])
def api_appointment():
    content = request.json
    return make_response(
        jsonify(
            message="Appointment created successfully",
            appointment=Appointment_business.set_appoitment(content),
        )
    )


app.run(debug=True)
