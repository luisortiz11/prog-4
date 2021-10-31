##Parcial #1
##Actividad: Crear una aplicación de línea de comandos que permita registro, 
# búsqueda, edición y eliminación de artículos dentro de un sistema de inventario.
##Nota: El código fuente debe ser subido a un repositorio en GitLab/Github. 
# En este espacio se sube el URL hacia el repositorio

import pymongo

# Establece conexion con servidor MongoDB
con = pymongo.MongoClient("mongodb://localhost:27017/")

db = con["inventorio"] # Base de datos
col = db["articulos"] # Coleccion

def menu():
    print("\nMENU PRINCIPAL")  
    print("1. Agregar nuevo articulo")  
    print("2. Editar articulo")  
    print("3. Eliminar articulo")
    print("4. Ver listado de articulos")
    print("5. Buscar articulo")
    print("6. Salir") 

def menuedit():
    print("\nATRIBUTO A EDITAR")  
    print("1. Nombre")  
    print("2. Precio")  
    print("3. Cantidad")
    print("4. Todos los atributos")
    print("5. Salir") 

def agg(a,b,c,d):
    art = { "_id": a, "articulo": b, "precio": c, "cantidad": d}
    col.insert_one(art)

def edit(a,b, opcion):
    query = {"articulo" : a}
    if opcion == 1:
        nuevo = {"$set": { "articulo" : b}}
        col.update_one(query, nuevo)
    if opcion == 2:
        nuevo = {"$set": { "precio" : b}}
        col.update_one(query, nuevo)
    if opcion == 3:
        nuevo = {"$set": { "cantidad" : b}}
        col.update_one(query, nuevo)
        
def delete(a):
   query = {"articulo" : a}
   col.delete_one(query)

def lista():
    for el in col.find():
        print(el)

def res(a):
    query = col.find_one({},{ "articulo": a})
    print(query)


# a) Agregar nueva palabra, c) Editar palabra existente, d) Eliminar palabra existente, e) Ver listado de palabras, f) Buscar significado de palabra, g) Salir

if __name__ == "__main__":
    ckey = 0;
    while True:
        menu()  
        opcion = int(input("Entre la opción (1-6):")) 

        if opcion == 1: 
            print("\nAGREGAR NUEVO ARTICULO")
            articulo = str(input("Articulo:"))
            precio = float(input("Precio:")) 
            cant =  int(input("Cantidad:")) 
            agg(ckey, articulo, precio, cant)
            ckey+=1
        elif opcion == 2:
            print("\nEDITAR ARTICULO EXISTENTE")
            pal = str(input("Articulo a editar:"))
            res(pal)
            menuedit()
            opcionedit = int(input("Entre la opción (1-6):"))
            if opcionedit == 1:
                newpal = str(input("Articulo editado:"))
                edit(pal, newpal, opcionedit)
            if opcionedit== 2:
                newprecio = float(input("Articulo editado:"))
                edit(pal, newprecio, opcionedit)
            if opcionedit == 3:
                newcant = int(input("Cantidad editada:"))
                edit(pal, newcant, opcionedit)
            if opcionedit == 4:
                newpal = str(input("Articulo editado:"))
                newprecio = float(input("Precio editado:"))
                newcant = int(input("Cantidad editada:"))
                agg(ckey, newpal, newprecio, newcant)
                delete(pal)
                ckey+=1
            if opcionedit == 5:
                break
        elif opcion == 3:
            print("\nELIMINAR ARTICULO EXISTENTE")
            art = str(input("Articulo a eliminar:"))
            delete(art)
        elif opcion == 4:
            print("\nLISTADO DE ARTICULOS")
            lista()
        elif opcion == 5:
            print("\nBUSCAR ARTICULO")
            art = str(input("Articulo:"))
            res(art)
        elif opcion ==6:
            con.db.command("dropDatabase")
            col.drop()
            break
        else:
            print("opcion no existe")






