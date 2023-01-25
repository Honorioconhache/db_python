import sqlite3

conn = sqlite3.connect('myBBDD')
puntero = conn.cursor()
#puntero.execute("CREATE TABLE PRODUCTOS(NARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")


try:
    puntero.execute("select * from productos")
    muchos_productos = puntero.fetchall()
    print(muchos_productos)
    #conn.commit()
    puntero.close()
except:
  print('FALLO')
  puntero.close()



conn.close()