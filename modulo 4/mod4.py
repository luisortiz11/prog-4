import redis

r = redis.StrictRedis(host= 'localhost', port= 6379, db= 0 )

def menu():
    print("\nMENU PRINCIPAL")  
    print("1. Agregar nueva palabra")  
    print("2. Editar palabra existente")  
    print("3. Eliminar palabra existente")
    print("4. Ver listado de palabras")
    print("5. Buscar significado de palabra")
    print("6. Salir") 
    
def agg(a,b):
    r.set(a, b)
    
def edit(a,b):
    sig = r.get(a)
    r.delete(a)
    r.set(b, sig)

def delete(a):
    r.delete(a)

def lista():
    for i in r.keys():
        sig = r.get(i)
        print(i, sig)

def res(a):
    print(r.get(a))
    
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
            agg(palabra, significado)
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
