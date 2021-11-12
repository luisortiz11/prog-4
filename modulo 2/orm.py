from sqlalchemy import ForeignKey, Table, Column, Integer, String, MetaData
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship

Base = declarative_base()

class Palabras(Base):
   __tablename__ = 'palabra'
   id = Column(Integer, primary_key=True)
   palabra = Column(String)
   defid = Column(Integer, ForeignKey('definicion.id'))
   definicion = relationship("Definiciones", back_populates = "palabra")

class Definiciones(Base):
   __tablename__ = 'definicion'
   id = Column(Integer, primary_key=True)
   definicion = Column(String)
   palabra = relationship("Palabras", back_populates = "definicion")
   
   
engine = create_engine('sqlite:///palabras.db', echo = True)

Session = sessionmaker(bind = engine)
session = Session()
meta = MetaData()

palabra = Table(
'palabra', meta, 
Column('id', Integer, primary_key = True), 
Column('palabra', String), 
Column('defid', Integer, ForeignKey('definicion.id')) 
)

definicion = Table(
'definicion', meta, 
Column('id', Integer, primary_key = True), 
Column('definicion', String)
)

meta.create_all(engine)

def menu():
    print("\nMENU PRINCIPAL")  
    print("1. Agregar nueva palabra")  
    print("2. Editar palabra existente")  
    print("3. Eliminar palabra existente")
    print("4. Ver listado de palabras")
    print("5. Buscar significado de palabra")
    print("6. Salir") 

def agg(a,b,c):
    Session = sessionmaker(bind = engine)
    session = Session()
    session.add(Palabras(id = a, palabra = b, defid = a))
    session.add(Definiciones(id = a, definicion = c))
    session.commit()
    session.close()

def edit(a,b):
    Session = sessionmaker(bind = engine)
    session = Session()
    par = session.query(Palabras).filter(Palabras.palabra == a).one()
    par.palabra = b
    session.commit()
    session.close()

def delete(a):
    Session = sessionmaker(bind = engine)
    session = Session()
    par = session.query(Palabras).filter(Palabras.palabra == a).one()
    session.delete(par)
    session.commit()
    session.close()

def lista():
    Session = sessionmaker(bind = engine)
    session = Session()
    
    for c, i in session.query(Palabras, Definiciones).filter(Palabras.id == Definiciones.id).all():
        print ("ID: {} Palabra: {} Definicion: {}".format(c.id,c.palabra, i.definicion))

    session.close()
 


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
        elif opcion ==6:
            break
        else:
            print("opcion no existe")