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
 
@app.route('/agregar',  methods=['GET', 'POST'])
def agregar():
   
   pal = str(request.form.get("palabra"))
   defn = str(request.form.get("significado"))
   agg(pal, defn)
   return '''<html><head><title>Agregar palabras</title></head>
   <body>
   <h1>Agrega una palabra</h1>
   <form  method="post" >
      <input name="palabra" type="text" placeholder="Entre el termino">
      <input name= "significado" type="text" placeholder="Entre el significado">
      <button type="submit" onclick={{ url_for( 'agregar') }}';">Post</button>
   </form>
   
   <form>
      <input type="button" value="Volver" onclick="history.back()">
   </form>
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
        <form method="post" >
          <input name="palabra" type="text" placeholder="Entre el termino">
          <input name= "editado" type="text" placeholder="Entre termino editado">
          <button type="submit" onclick={{ url_for( 'editar') }}';">Post</button>
        </form>
         <form>
            <input type="button" value="Volver" onclick="history.back()">
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
        <form method="post" >
          <input name="palabra" type="text" placeholder="Entre el termino">
          <button type="submit" onclick={{ url_for( 'eliminar') }}';">Post</button>
        </form>
         <form>
            <input type="button" value="Volver" onclick="history.back()">
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
      <h2>{lista}</h2>

      <form>
         <input type="button" value="Volver" onclick="history.back()">
      </form>
    </body>
</html>'''.format(lista=lista)

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
          <button stype="submit" onclick={{ url_for( 'buscar') }}';">Post</button>
        </form>
      <h2>Resultado</h2>
      <h3>{pal}:{resultado}</h3>
      <form>
         <input type="button" value="Volver" onclick="history.back()">
      </form>
    </body>
</html>'''.format(pal=pal, resultado=resultado)
   else:
      return '''<html>
    <head>
        <title>Buscar palabras</title>
    </head>
    <body>
      <h1>Buscar una palabra</h1>
        <form method="post" >
          <input name="palabra" type="text" placeholder="Entre el termino">
          <button type="submit" onclick={{ url_for( 'buscar') }}';">Post</button>
        </form>
         <form>
            <input type="button" value="Volver" onclick="history.back()">
         </form>
    </body>
</html>''' 


if __name__ == '__main__':
   app.debug = True
   app.run()
   app.run(debug = True)