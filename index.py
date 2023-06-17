from flask import Flask, jsonify, make_response, request
from src.business.Appointmente_business import Appointment_business
from src.business.Professional_business import Professional_business

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
    try:
        content = request.json
        return make_response(
            jsonify(
                message="Appointment created successfully",
                appointment=Appointment_business.set_appoitment(content),
            )
        )
    except ValueError as erro:
        return make_response(jsonify(str(erro)), 400)
    except Exception as erro:
        return make_response(jsonify(str(erro)), 500)


@app.route("/professional", methods=["POST"])
def api_professional():
    try:
        name = request.json["name"]
        social_name = request.json.get("social_name", "")

        content = {"name": name, "social_name": social_name}

        return make_response(
            jsonify(
                message="Registered professional",
                professional=Professional_business.create_professional(content),
            )
        )
    except ValueError as erro:
        return make_response(jsonify(str(erro)), 400)
    except Exception:
        return make_response(jsonify(str(Exception)), 500)


@app.route("/professional/<id>", methods=["PUT", "DELETE"])
def api_professiona_id(id):
    try:
        if request.method == "PUT":
            name = request.json.get("name", "")
            social_name = request.json.get("social_name", "")

            content = {"name": name, "social_name": social_name}
            return make_response(
                jsonify(
                    message="Professional updated successfully",
                    professional=Professional_business.update_professional(id, content),
                )
            )
        elif request.method == "DELETE":
            return make_response(
                jsonify(message=Professional_business.delete_professional(id))
            )
    except ValueError as erro:
        return make_response(jsonify(str(erro)), 400)
    except FileNotFoundError as erro:
        return make_response(jsonify(str(erro)), 404)
    except Exception as erro:
        return make_response(jsonify(str(erro)), 500)


app.run(debug=True)
