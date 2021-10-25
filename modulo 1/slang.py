#Elaborar una aplicación de línea de comandos en Python 
# que sirva cuyo propósito sea mantener un diccionario de 
# palabras del slang panameño (xopa, mopri, otras). 
# Las palabras y su significado deben ser almacenadas dentro 
# de una base de datos SQLite. Las opciones dentro del programa 
# deben incluir como mínimo: 
# a) Agregar nueva palabra, c) Editar palabra existente, 
# d) Eliminar palabra existente, e) Ver listado de palabras, 
# f) Buscar significado de palabra, g) Salir

import sqlite3

#
def menu():
    print("\nMENU PRINCIPAL")  
    print("1. Agregar nueva palabra")  
    print("2. Editar palabra existente")  
    print("3. Eliminar palabra existente")
    print("4. Ver listado de palabras")
    print("5. Buscar significado de palabra")
    print("6. Salir") 

def base():
    conn = sqlite3.connect('dict.db')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE dict
                (id         INTEGER PRIMARY KEY,
                PALABRA    TEXT NOT NULL,
                DEFINICION  TEXT NOT NULL)''')
    conn.commit()
    conn.close()

def popular():
    with open("prog-4\slang_pan.txt") as f:
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

    
def agg(a,b,c):
    conn = sqlite3.connect('dict.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO dict(id, palabra, definicion) VALUES (?, ?, ?)", (a, b, c))
    conn.commit()
    conn.close()

def edit(a,b):
    conn = sqlite3.connect('dict.db')
    cur = conn.cursor()
    cur.execute('''UPDATE dict SET palabra = ? WHERE palabra = ?''', (b, a))
    conn.commit()
    conn.close()

def delete(a):
    conn = sqlite3.connect('dict.db')
    cur = conn.cursor()
    cur.execute("DELETE from dict where palabra = ?", (a,))
    conn.commit()
    conn.close()

def lista():
    conn = sqlite3.connect('dict.db')
    cur = conn.cursor()
    cur.execute("SELECT * from dict")
    for i in cur.fetchall(): 
        print("{}. {}:{}".format(*i))
    conn.close()

def res(a):
    conn = sqlite3.connect('dict.db')
    cur = conn.cursor()
    cur.execute("SELECT definicion FROM dict WHERE palabra LIKE ? || '%' ", (a,))
    for i in cur.fetchall(): 
        print(":{}".format(*i))
    conn.close()

# a) Agregar nueva palabra, c) Editar palabra existente, d) Eliminar palabra existente, e) Ver listado de palabras, f) Buscar significado de palabra, g) Salir

if __name__ == "__main__":
    base()
    ckey = popular()

    while True:
        menu()  
        opcion = int(input("Entre la opción (1-6):")) 

        if opcion == 1: 
            print("\nAGREGAR NUEVA PALABRA")
            palabra = str(input("Nueva palabra:"))
            significado = str(input("Significado:")) 
            agg(ckey, palabra, significado)
            ckey+=1
        elif opcion == 2:
            print("\nEDITAR PALABRA EXISTENTE")
            pal = str(input("Palabra a editar:"))
            newpal = str(input("Palabra editada:"))
            edit(pal, newpal)
        elif opcion == 3:
            print("\nELIMINAR PALABRA EXISTENTE")
            pala = str(input("Palabra a eliminar:"))
            delete(pala)
        elif opcion == 4:
            print("\nListado de palabras")
            lista()
        elif opcion == 5:
            print("\nBUSCAR SIGNIFICADO DE PALABRA")
            pala = str(input("Palabra a buscar:"))
            res(pala)
        elif opcion ==6:
            break
        else:
            print("opcion no existe")