from distutils.log import debug
from re import S
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route ('/Me_Ki/<string:metros>')
def funMeaKi(metros):
    metros=float(metros)
    kilometros=float(3.6)
    resultado=metros*kilometros
    return jsonify({"resultado": resultado})

@app.route('/Me_Mi/<string:metros>')
def funMeaMi(metros):
    metros=float(metros)
    millas=float(2.23693)
    resultado=metros*millas
    return jsonify({"resultado": resultado})

@app.route('/Ki_Me/<string:kilometros>')
def funKiaMe(kilometros):
    kilometros=float(kilometros)
    metros=float(0.27778)
    resultado=kilometros*metros
    return jsonify({"resultado": resultado})

@app.route('/Ki_Mi/<string:kilometros>')
def funKiaMi(kilometros):
    kilometros=float(kilometros)
    millas=float(0.62137)
    resultado=kilometros*millas
    return jsonify({"resultado": resultado})

@app.route('/Mi_Me/<string:millas>')
def funMiaMe(millas):
    millas=float(millas)
    metros=float(0.27778)
    resultado=kilometros*metros
    return jsonify({"resultado": resultado})

@app.route('/Mi_ki/<string:millas>')
def funMiaKi(millas):
    millas=float(millas)
    kilometros=float(0.27778)
    resultado=kilometros*millas
    return jsonify({"resultado": resultado})

if __name__== '__main__':
    app.run(debug=True, port=4000)