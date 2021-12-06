#Elaborar una aplicación de línea de comandos en Python 
# que sirva cuyo propósito sea mantener un diccionario de 
# palabras del slang panameño (xopa, mopri, otras). 
# Las palabras y su significado deben ser almacenadas dentro 
# de una base de datos SQLite. Las opciones dentro del programa 
# deben incluir como mínimo: 
# a) Agregar nueva palabra, c) Editar palabra existente, 
# d) Eliminar palabra existente, e) Ver listado de palabras, 
# f) Buscar significado de palabra, g) Salir

# Importar modulo de SQLite para python
import sqlite3

# Funcion menu: imprime la interfaz de linea de comandos
def menu():
    print("\nMENU PRINCIPAL")  
    print("1. Agregar nueva palabra")  
    print("2. Editar palabra existente")  
    print("3. Eliminar palabra existente")
    print("4. Ver listado de palabras")
    print("5. Buscar significado de palabra")
    print("6. Salir") 

#Funcion base: crea la conexion a la base de datos sqlite,
# crea una tabla 'dict' con columnas id, palabra y definicion
# salva los cambios y cierra la conexion.
def base():
    conn = sqlite3.connect('dictmod1.db')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE if not exists dict
                (id         INTEGER PRIMARY KEY,
                PALABRA    TEXT NOT NULL,
                DEFINICION  TEXT NOT NULL)''')
    conn.commit()
    conn.close()

#Funcion popular: extrae slang panameño de un archivo de texto plano existente,
# crea una conexion con la base de datos y llena la tabla de la base de datos
# salva los cambios y cierra la conexion.
# Retorna la ultima llave primaria de la tabla.
def popular():
    with open("modulo 1\slang_pan.txt") as f:
        contenido = f.read().splitlines()
    
    conn = sqlite3.connect('dict.db')
    cur = conn.cursor()

    key = 0
    for j in contenido:
        a = j.split('=')
        cur.execute("INSERT INTO dict(id, palabra, definicion) VALUES (?, ?, ?)", (key, a[0].lstrip(), a[1].strip()))
        key+=1
    
    conn.commit()
    conn.close()
    return key 

#Funcion agg: se conecta con la base de datos e inserta a la tabla dict,
# los argumentos de la funcion. Por lo tanto, los argumentos de la funcion
# deben ser id, palabra y definicion, en ese orden.
# salva los cambios y cierra la conexion.
def agg(a,b,c):
    conn = sqlite3.connect('dict.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO dict(id, palabra, definicion) VALUES (?, ?, ?)", (a, b, c))
    conn.commit()
    conn.close()

#Funcion edit: se conecta a la base de datos y actualiza el valor de alguna fila, segun
# el criterio 'palabra'. Cambia dicho valor por el otro argumento de la funcion.
# salva los cambios y cierra la conexion.
def edit(a,b):
    conn = sqlite3.connect('dict.db')
    cur = conn.cursor()
    cur.execute('''UPDATE dict SET palabra = ? WHERE palabra = ?''', (b, a))
    conn.commit()
    conn.close()

#Funcion delete: se conecta a la base de datos y borra alguna fila, segun
# el criterio 'palabra'. Salva los cambios y cierra la conexion.
def delete(a):
    conn = sqlite3.connect('dict.db')
    cur = conn.cursor()
    cur.execute("DELETE from dict where palabra = ?", (a,))
    conn.commit()
    conn.close()

#Funcion lista: se conecta a la base de datos e imprime todos los elementos de la tabla
# se aplica un formato de impresion especifico, tal que cada elemento se imprime de la forma
# id. palabra: defincion
# Se cierra la conexion.
def lista():
    conn = sqlite3.connect('dict.db')
    cur = conn.cursor()
    cur.execute("SELECT * from dict")
    for i in cur.fetchall(): 
        print("{}. {}:{}".format(*i))
    conn.close()

#Funcion resultado: se conecta a la base de datos y se busca la definicion de alguna palabra,
# usando como criterio la misma palabra. 
# se imprimen todos los resultados de la forma 
# :definicion
# se cierra la conexion
def res(a):
    conn = sqlite3.connect('dict.db')
    cur = conn.cursor()
    cur.execute("SELECT definicion FROM dict WHERE palabra LIKE ? || '%' ", (a,))
    for i in cur.fetchall(): 
        print(":{}".format(*i))
    conn.close()

# Se cumple con los requerimientos de 
# a) Agregar nueva palabra, c) Editar palabra existente, d) Eliminar palabra existente, 
# e) Ver listado de palabras, f) Buscar significado de palabra, g) Salir

if __name__ == "__main__":
    
    base() #Llama a la funcion base para crear la conexion con la base de datos y la tabla dict
    
    ckey = popular() #Llama a la funcion popular que llena la tabla con palabras y sus definiciones a partir de un documento
    # de texto plano y retorna la ultima llave primaria (id) de la tabla, 
    # Guarda dicha ultima id en la variable 'ckey'

    while True: # Ciclo perpetuo para la ejecucion del programa en linea de comandos
        menu() # Imprime el menu principal  
        opcion = int(input("Entre la opción (1-6):")) #Imprime para pedir elegir alguna opcion numerica del menu principal.

        # Estructura de control (tipo switch) a partir de multiples if
        if opcion == 1: #Imprime titulo de submenu y consulta los valores de palabra y definicion para agregarlos a la base de datos 
            print("\nAGREGAR NUEVA PALABRA")
            palabra = str(input("Nueva palabra:"))
            significado = str(input("Significado:")) 
            agg(ckey, palabra, significado)
            ckey+=1
        elif opcion == 2: #Imprime titulo de submenu y consulta los valores de palabra a editar y palabra nueva
            print("\nEDITAR PALABRA EXISTENTE")
            pal = str(input("Palabra a editar:"))
            newpal = str(input("Palabra editada:"))
            edit(pal, newpal)
        elif opcion == 3:  #Imprime titulo de submenu y consulta el valor de palabra a eliminar
            print("\nELIMINAR PALABRA EXISTENTE")
            pala = str(input("Palabra a eliminar:"))
            delete(pala)
        elif opcion == 4: #Imprime titulo de submenu y todas los tripletas id, palabra, definicion de la tabla de la bd
            print("\nListado de palabras")
            lista()
        elif opcion == 5: #Imprime submenu y consulta el valor de palabra para buscar su definicion 
            print("\nBUSCAR SIGNIFICADO DE PALABRA")
            pala = str(input("Palabra a buscar:"))
            res(pala)
        elif opcion ==6: #Salir del programa
            break
        else:
            print("opcion no existe") # Control de excepciones en la elecion de la opcion del menu principal