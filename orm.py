import sqlalchemy as db

engine = db.create_engine('sqlite:///ejemplo.db')
conn = engine.connect()
metadata = db.MetaData()
persona = db.Table('ejemplo', metadata, autoload=True, autoload_with = engine)

print(persona.columns.keys())
print(repr(metadata.tables['ejemplo']))

query = db.select([persona])
resultado = conn.execute(query).fetchall()

print(resultado)


query = db.select([persona]).where(persona.columns.SALARIO > 20000 )
resultado = conn.execute(query).fetchall()
print(resultado)
