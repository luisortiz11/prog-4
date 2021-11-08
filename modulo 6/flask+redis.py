from flask import Flask
from flask import request
from flask import render_template
import redis

app = Flask(__name__)
r = redis.StrictRedis(host= 'localhost', port= 6379, db= 0, charset="utf-8", decode_responses=True)

def agg(a,b):
   r.set(a, b)

def edit(a,b):
   sig = str(r.get(a))
   r.set(b, sig)
   delete(a)

def delete(a):
   r.delete(a)

def res(a):
   return r.get(a)

@app.route('/')
def menu():
   return render_template("menu.html")
 
@app.route('/agregar',  methods=['GET'])
def agregar():
   if str(request.args.get("palabra")) != "None" and str(request.args.get("significado")) != "None" :
      pal = str(request.args.get("palabra"))
      defn = str(request.args.get("significado"))
      agg(pal, defn)
   return render_template("agregar.html")

@app.route('/editar',  methods=['GET', 'POST'])
def editar():
   pal = str(request.form.get("palabra"))
   pale = str(request.form.get("editado"))
   edit(pal, pale)
   return render_template("editar.html")

@app.route('/eliminar',  methods=['GET', 'POST'])
def eliminar():
   pal = str(request.form.get("palabra"))
   delete(pal)
   return render_template("eliminar.html")

@app.route('/listado',  methods=['GET', 'POST'])
def listado():
   lista = {}
   for i in r.keys():
      sig = r.get(i)
      lista[i] = sig   
   return render_template("listado.html", diccion=lista.items())

@app.route('/buscar',  methods=['GET', 'POST'])
def buscar():
   
   pal = str(request.form.get("palabra"))
   resultado = res(pal)
   if pal != "" and pal!="None":
      return render_template("buscar.html",b=pal, x=resultado)
   else:
      return render_template("buscar.html")


if __name__ == '__main__':
   app.debug = True
   app.run()
   app.run(debug = True)