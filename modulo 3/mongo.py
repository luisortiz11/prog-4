import pymongo
import random

# Establece conexion con servidor MongoDB
con = pymongo.MongoClient("mongodb://localhost:27017/")

db = con["mongomod3"] # Base de datos
col = db["terminos"] # Coleccion

def menu():
    print("\nMENU PRINCIPAL")  
    print("1. Agregar nueva palabra")  
    print("2. Editar palabra existente")  
    print("3. Eliminar palabra existente")
    print("4. Ver listado de palabras")
    print("5. Buscar significado de palabra")
    print("6. Salir") 

def agg(a,b,c):
    palabra = { "_id": a, "termino": b, "significado": c}
    col.insert_one(palabra)

def edit(a,b):
    query = {"termino" : a}
    nuevo = {"$set": { "termino" : b}}
    col.update_one(query, nuevo)

def delete(a):
   query = {"termino" : a}
   col.delete_one(query)

def lista():
    for el in col.find():
        print(el)

def res(a):
    query = col.find_one({"termino" : a})
    print(query)


# a) Agregar nueva palabra, c) Editar palabra existente, d) Eliminar palabra existente, e) Ver listado de palabras, f) Buscar significado de palabra, g) Salir

if __name__ == "__main__":
    ckey = 0
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

