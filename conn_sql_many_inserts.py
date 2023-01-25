import sqlite3

conn = sqlite3.connect('myBBDD')
puntero = conn.cursor()
#puntero.execute("CREATE TABLE PRODUCTOS(NARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")

muchos_productos = [
    ("Guayos",100,"Deportes"),
    ("Camisa",150,"Ejecutivo"),
    ("Cadena",1000,"Joyas")
]

try:
    puntero.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", muchos_productos)
    conn.commit()
    puntero.close()
except:
  print('FALLO')
  puntero.close()



conn.close()