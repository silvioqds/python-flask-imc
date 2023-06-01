from flask import Flask, jsonify, request
from models.person import Person
from services.imc import calculate

app = Flask(__name__)

@app.route('/imc/calculate', methods=['POST'])
def calculate_imc():
    p = Person.from_dict(request.json)  
    calculate(p)
    return jsonify(p.to_dict())


app.run(host='127.0.0.1', port=8080, debug=True)