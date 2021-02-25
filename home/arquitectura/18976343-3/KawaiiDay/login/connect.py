import pymysql

con = pymysql.connect('167.86.114.135','arqui_kawaiiappuser','kawaiiapp123','arqui_kawaii')
def connection():

        # prepare a cursor object using cursor() method
        try:
            with con.cursor() as cur:
                cur.execute('SELECT VERSION()')
                version = cur.fetchone()
                print("Database version: .'version[0]'.")
        finally:
            print("conectado")

def consultar(sqlquery):
        try:
            with con.cursor() as cur:
                cur.execute(sqlquery)
                return cur.fetchall()
        finally:
            print("conectado")

def modificar(sqlquery):
        try:
            with con.cursor() as cur:
                cur.execute(sqlquery)
                return cur.fetchall()
        finally:
            print("modificado")

def cerrar():
    try:
        con.close()
        connect.close()
        print("Conexion con base de datos cerrada")
    except:
        print("Error al cerrar conexion")


def llenado(largo):
    aux = str(largo)
    while len(aux) < 5:
        aux = '0' + aux
    print(aux)
    return aux


connection()
