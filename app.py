from distutils.log import debug
from flask import Flask
from flask import Flask, jsonify

app = Flask(__name__)



#//////////////////////////////////METROS///////////////////////////////////////



@app.route ('/Me_Me/<string:metros>')
def Me_Me(metros):
    resultado=metros
    return jsonify({"resultado": resultado})

@app.route ('/Me_Ki/<string:metros>')
def Me_Ki(metros):
    metros=float(metros)
    kilometros=float(3.6)
    resultado=metros*kilometros
    return jsonify({"resultado": resultado})

@app.route ('/Me_Nu/<string:metros>')
def Me_Nu(metros):
    metros=float(metros)
    nudos=float(1.94384)
    resultado=metros*nudos
    return jsonify({"resultado": resultado})

@app.route('/Me_Mi/<string:metros>')
def Me_Mi(metros):
    metros=float(metros)
    millas=float(2.23693)
    resultado=metros*millas
    return jsonify({"resultado": resultado})

@app.route ('/Me_Pi/<string:metros>')
def Me_Pi(metros):
    metros=float(metros)
    pies=float(3.28083)
    resultado=metros*pies
    return jsonify({"resultado": resultado})

@app.route ('/Me_Pu/<string:metros>')
def Me_Pu(metros):
    metros=float(metros)
    pulgadas=float(39.37007)
    resultado=metros*pulgadas
    return jsonify({"resultado": resultado})



    #//////////////////////////////////KILOMETROS///////////////////////////////////////



@app.route('/Ki_Me/<string:kilometros>')
def Ki_Me(kilometros):
    kilometros=float(kilometros)
    metros=float(0.27778)
    resultado=kilometros*metros
    return jsonify({"resultado": resultado})

@app.route('/Ki_Ki/<string:kilometros>')
def Ki_Ki(kilometros):
    kilometros=float(kilometros)
    resultado=kilometros
    return jsonify({"resultado": resultado})

@app.route('/Ki_Nu/<string:kilometros>')
def Ki_Nu(kilometros):
    kilometros=float(kilometros)
    nudos=float(0.53995)
    resultado=kilometros*nudos
    return jsonify({"resultado": resultado})

@app.route('/Ki_Mi/<string:kilometros>')
def Ki_Mi(kilometros):
    kilometros=float(kilometros)
    millas=float(0.62137)
    resultado=kilometros*millas
    return jsonify({"resultado": resultado})

@app.route('/Ki_Pi/<string:kilometros>')
def Ki_Pi(kilometros):
    kilometros=float(kilometros)
    pies=float(0.91134)
    resultado=kilometros*pies
    return jsonify({"resultado": resultado})

@app.route('/Ki_Pu/<string:kilometros>')
def Ki_Pu(kilometros):
    kilometros=float(kilometros)
    pulgadas=float(10.93613)
    resultado=kilometros*pulgadas
    return jsonify({"resultado": resultado})



#//////////////////////////////////NUDOS///////////////////////////////////////



@app.route('/Nu_Me/<string:nudos>')
def Nu_Me(nudos):
    nudos=float(nudos)
    metros=float(0.51444)
    resultado=nudos*metros
    return jsonify({"resultado": resultado})

@app.route('/Nu_Ki/<string:nudos>')
def Nu_Ki(nudos):
    nudos=float(nudos)
    kilometros=float(1.852)
    resultado=nudos*kilometros
    return jsonify({"resultado": resultado})

@app.route('/Nu_Nu/<string:nudos>')
def Nu_Nu(nudos):
    nudos=float(nudos)
    resultado=nudos
    return jsonify({"resultado": resultado})

@app.route('/Nu_Mi/<string:nudos>')
def Nu_Mi(nudos):
    nudos=float(nudos)
    millas=float(1.15077)
    resultado=nudos*millas
    return jsonify({"resultado": resultado})

@app.route('/Nu_Pi/<string:nudos>')
def Nu_Pi(nudos):
    nudos=float(nudos)
    pies=float(1.6878)
    resultado=nudos*pies
    return jsonify({"resultado": resultado})

@app.route('/Nu_Pu/<string:nudos>')
def Nu_Pu(nudos):
    nudos=float(nudos)
    pulgadas=float(20.25371)
    resultado=nudos*pulgadas
    return jsonify({"resultado": resultado})


#//////////////////////////////////MILLAS///////////////////////////////////////



@app.route('/Mi_Me/<string:millas>')
def Mi_Me(millas):
    millas=float(millas)
    metros=float(0.27778)
    resultado=millas*metros
    return jsonify({"resultado": resultado})

@app.route('/Mi_Ki/<string:millas>')
def Mi_Ki(millas):
    millas=float(millas)
    kilometros=float(0.27778)
    resultado=millas*kilometros
    return jsonify({"resultado": resultado})

@app.route('/Mi_Nu/<string:millas>')
def Mi_Nu(millas):
    millas=float(millas)
    nudos=float(0.27778)
    resultado=millas*nudos
    return jsonify({"resultado": resultado})

@app.route('/Mi_Mi/<string:millas>')
def Mi_Mi(millas):
    millas=float(millas)
    resultado=millas
    return jsonify({"resultado": resultado})

@app.route('/Mi_Pi/<string:millas>')
def Mi_Pi(millas):
    millas=float(millas)
    pies=float(0.27778)
    resultado=millas*pies
    return jsonify({"resultado": resultado})

@app.route('/Mi_Pu/<string:millas>')
def Mi_Pu(millas):
    millas=float(millas)
    pulgadas=float(0.27778)
    resultado=millas*pulgadas
    return jsonify({"resultado": resultado})



#//////////////////////////////////PIES///////////////////////////////////////



@app.route('/Pi_Me/<string:pies>')
def Pi_Me(pies):
    pies=float(pies)
    metros=float(0.3048)
    resultado=pies*metros
    return jsonify({"resultado": resultado})

@app.route('/Pi_Ki/<string:pies>')
def Pi_Ki(pies):
    pies=float(pies)
    kilometros=float(1.09728)
    resultado=pies*kilometros
    return jsonify({"resultado": resultado})

@app.route('/Pi_Nu/<string:pies>')
def Pi_Nu(pies):
    pies=float(pies)
    nudos=float(0.59248)
    resultado=pies*nudos
    return jsonify({"resultado": resultado})

@app.route('/Pi_Mi/<string:pies>')
def Pi_Mi(pies):
    pies=float(pies)
    millas=float(0.68181)
    resultado=pies*millas
    return jsonify({"resultado": resultado})

@app.route('/Pi_Pi/<string:pies>')
def Pi_Pi(pies):
    pies=float(pies)
    resultado=pies
    return jsonify({"resultado": resultado})

@app.route('/Pi_Pu/<string:pies>')
def Pi_Pu(pies):
    pies=float(pies)
    pulgadas=float(12)
    resultado=pies*pulgadas
    return jsonify({"resultado": resultado})



#//////////////////////////////////PULGADAS///////////////////////////////////////



@app.route('/Pu_Me/<string:pulgadas>')
def Pu_Me(pulgadas):
    pulgadas=float(pulgadas)
    metros=float(0.0254)
    resultado=pulgadas*metros
    return jsonify({"resultado": resultado})

@app.route('/Pu_Ki/<string:pulgadas>')
def Pu_Ki(pulgadas):
    pulgadas=float(pulgadas)
    kilometros=float(0.09144)
    resultado=pulgadas*kilometros
    return jsonify({"resultado": resultado})

@app.route('/Pu_Nu/<string:pulgadas>')
def Pu_Nu(pulgadas):
    pulgadas=float(pulgadas)
    nudos=float(0.04937)
    resultado=pulgadas*nudos
    return jsonify({"resultado": resultado})

@app.route('/Pu_Mi/<string:pulgadas>')
def Pu_Mi(pulgadas):
    pulgadas=float(pulgadas)
    millas=float(0.05681)
    resultado=pulgadas*millas
    return jsonify({"resultado": resultado})

@app.route('/Pu_Pi/<string:pulgadas>')
def Pu_Pi(pulgadas):
    pulgadas=float(pulgadas)
    pies=float(12)
    resultado=pulgadas*pies
    return jsonify({"resultado": resultado})

@app.route('/Pu_Pu/<string:pulgadas>')
def Pu_Pu(pulgadas):
    pulgadas=float(pulgadas)
    resultado=pulgadas
    return jsonify({"resultado": resultado})

if __name__ == '__main__':
    app.run(debug=True, port=4000)