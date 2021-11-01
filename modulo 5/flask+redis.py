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


@app.route('/',  methods=['GET', 'POST'])
def menu():
   return render_template("menu.html")

##action 
@app.route('/agregar',  methods=['GET', 'POST'])
def agregar():
   pal = str(request.form.get("palabra", False))
   defn = str(request.form.get("significado", False))
   agg(pal, defn)
   return render_template("agregar.html")

@app.route('/editar',  methods=['GET', 'POST'])
def editar():
   pal = str(request.form.get("palabra", False))
   pale = str(request.form.get("editado", False))
   edit(pal, pale)
   return render_template("editar.html")

@app.route('/eliminar',  methods=['GET', 'POST'])
def eliminar():
   pal = str(request.form.get("palabra", False))
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
   pal = str(request.form.get("palabra", False))
   resultado = res(pal)
   return render_template("buscar.html",b=pal, x=resultado)


if __name__ == '__main__':
   app.debug = True
   app.run()
   app.run(debug = True)