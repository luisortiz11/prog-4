from flask import Flask, redirect, request, url_for
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
   return '''<html>
   <body><h1>Diccionario slang panameño</h1>
   <nav>
   <div><a href="agregar">AGREGAR </a></div>
   <div><a href="editar">EDITAR </a></div>
   <div><a href="eliminar">ELIMINAR </a></div>
   <div><a href="listado">VER LISTADO</a></div>
   <div><a href="buscar">BUSCAR </a></div>
   </nav>
   </body>
   </html>'''
 
@app.route('/agregar',  methods=['GET'])
def agregar():
   if str(request.args.get("palabra")) != "None" and str(request.args.get("significado")) != "None" :
      pal = str(request.args.get("palabra"))
      defn = str(request.args.get("significado"))
      agg(pal, defn)
   return '''<html><head><title>Agregar palabras</title></head>
   <body>
   <h1>Agrega una palabra</h1>
   <input name="palabra" type="text" placeholder="Entre el termino">
   <input name= "significado" type="text" placeholder="Entre el significado">
   <button class="btn btn-default" type="submit">Post</button>
   </body>
   </html>'''

@app.route('/editar',  methods=['GET', 'POST'])
def editar():
   pal = str(request.form.get("palabra"))
   pale = str(request.form.get("editado"))
   edit(pal, pale)
   return '''
   <html>
    <head>
        <title>Editar palabras</title>
    </head>
    <body>
      <h1>Edita una palabra</h1>
        <form action="{{ url_for('editar') }}" method="post" >
          <input name="palabra" type="text" placeholder="Entre el termino">
          <input name= "editado" type="text" placeholder="Entre termino editado">
          <button class="btn btn-default" type="submit">Post</button>
        </form>
    </body>
   </html>
   
   '''

@app.route('/eliminar',  methods=['GET', 'POST'])
def eliminar():
   pal = str(request.form.get("palabra"))
   delete(pal)
   return '''
   <html>
    <head>
        <title>Eliminar palabras</title>
    </head>
    <body>
      <h1>Elimina una palabra</h1>
        <form action="{{ url_for('eliminar') }}" method="post" >
          <input name="palabra" type="text" placeholder="Entre el termino">
          <button class="btn btn-default" type="submit">Post</button>
        </form>
    </body>
   </html>
   '''

@app.route('/listado',  methods=['GET', 'POST'])
def listado():
   lista = {}
   for i in r.keys():
      sig = r.get(i)
      lista[i] = sig   
   return '''<html>
    <head>
        <title>Listado de palabras</title>
    </head>
    <body>
    <h1>Listado de palabras</h1>

    </body>
</html>'''

@app.route('/buscar',  methods=['GET', 'POST'])
def buscar():
   
   pal = str(request.form.get("palabra"))
   resultado = res(pal)
   if pal != "" and pal!="None":
      return   '''<html>
    <head>
        <title>Buscar palabras</title>
    </head>
    <body>
      <h1>Buscar una palabra</h1>
        <form method="post" >
          <input name="palabra" type="text" placeholder="Entre el termino">
          <button class="btn btn-default" type="submit" onclick={{ url_for( 'buscar') }}';">Post</button>
        </form>
    </body>
</html>'''
   else:
      return '''<html>
    <head>
        <title>Buscar palabras</title>
    </head>
    <body>
      <h1>Buscar una palabra</h1>
        <form method="post" >
          <input name="palabra" type="text" placeholder="Entre el termino">
          <button class="btn btn-default" type="submit" onclick={{ url_for( 'buscar') }}';">Post</button>
        </form>
    </body>
</html>'''


if __name__ == '__main__':
   app.debug = True
   app.run()
   app.run(debug = True)