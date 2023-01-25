import sqlite3

conn = sqlite3.connect('myBBDD')
puntero = conn.cursor()
#puntero.execute("CREATE TABLE PRODUCTOS(NARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")

try:
    puntero.execute("INSERT INTO PRODUCTOS VALUES('CAMISETA', 100, 'MODA')")
    print('DATOS INGRESADOS CORRECTAMENTE BD')
    conn.commit()
except:
  print('FALLO')

conn.close()