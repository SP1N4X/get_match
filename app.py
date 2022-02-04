from flask import Flask, request
import cal_result
from flask_cors import CORS

app = Flask('')
CORS(app)


@app.route('/')

def index():
    return "<h1>Welcome to our server !!</h1>"


@app.route('/post', methods=['POST'])

def result():
    ale = request.get_json()
    print(ale)
    risultato = cal_result.cal(ale)
    print(risultato)
    return risultato
