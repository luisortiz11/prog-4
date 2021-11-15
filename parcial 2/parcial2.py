#Descargue la fuente de datos relacionada con vacunación contra el sarampión en niños
#entre 12-23 meses en Panamá del Word Bank y diseñe un API tipo REST de sólo-lectura 
# que manipule estos datos.

import csv,random
from flask import Flask, request, render_template, jsonify
import pymongo

# Establece conexion con servidor MongoDB
con = pymongo.MongoClient("mongodb://localhost:27017/")

db = con["parcial2"] # Base de datos
col = db["bancovac"] # Coleccion

app = Flask(__name__)

with open('parcial 2\API_SH.IMM.MEAS_DS2_en_csv_v2_3165446\API_SH.IMM.MEAS_DS2_en_csv_v2_3165446.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    pan = []
    titulo = []
    for row in csv_reader:
        if (row['ï»¿"Data Source"'] == "Country Name"):
            for name in row.values():
                titulo.append(name)
        if (row['ï»¿"Data Source"'] == "Panama"):
            for data in row.values():
                pan.append(data)

data = dict(zip(titulo[:3], pan[:3])) | dict(zip(titulo[-1], pan[-1]))


def agg(b,c):
    a = random.randint(0,99999)
    palabra = { "_id": a, "key": b, "value": c}
    col.insert_one(palabra)


def res(a):
    query = col.find_one({"key": a})
    return query




@app.route('/')
def menu():
    col.remove({})
    sentinel = 0
    if (sentinel==0):
        for b,c in data.items():
            agg(b,c)
        sentinel+=1
    return render_template("menu.html")
 
@app.route('/api/<int:number>/',  methods=['GET', 'POST'])
def vacunas(number):
    query = res(str(number))
    return jsonify(query)

@app.route('/listado',  methods=['GET', 'POST'])
def listado(): 
   return render_template("listado.html", diccion=col.find({},{"_id": 0, "key": 1, "value": 1}))

@app.route('/buscar',  methods=['GET', 'POST'])
def buscar():
    yr = str(request.form.get("palabra"))
    resultado = res(yr)
    return render_template("buscar.html", b=yr, x=resultado)


if __name__ == '__main__':
    
   app.debug = True
   app.run()
   app.run(debug = True)