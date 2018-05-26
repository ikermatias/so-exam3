from flask import Flask
import json
import sys

sys.path.append('/home/sebastian/Escritorio/so-exam3/A00329796/')


from op_stats.datosPc import Datos

app = Flask(__name__)

@app.route('/darDatos/cpu')
def darPorcentajePc():
	porcentaje = Datos.darPorcentajeCpu()
	return json.dumps({'Porcentaje cpu': porcentaje})

@app.route('/darDatos/memoriaram')
def darMemoria():
        memoria = Datos.darMemoriaRam()
        return json.dumps({'Memoria ram': memoria})

@app.route('/darDatos/espaciolibre')
def darEspacioDisco():
        espacio = Datos.darEspacioLibreDisco()
        return json.dumps({'Espacio disponible': espacio})

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=8080)
