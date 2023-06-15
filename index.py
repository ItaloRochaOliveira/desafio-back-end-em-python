from flask import Flask, jsonify, make_response, request

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False

professional = [{"id": 1, "nome": "fernanda"}]

consultas = [{"id": 1, "nome": "Fernanda", "professional_id": 1, "data": "01/02/2024"}]


@app.route("/", methods=["GET"])
def get_consultas():
    return make_response(jsonify(consultas))


@app.route("/inquire", methods=["POST"])
def set_consultas():
    print("funciona")
    consulta = request.json
    consultas.append(consulta)
    return make_response(jsonify(message="Cadastrado com sucesso", consulta=consulta))


app.run()
