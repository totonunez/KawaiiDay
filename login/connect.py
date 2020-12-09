import pymysql


def connection():
        con = pymysql.connect('167.86.114.135','arqui_kawaiiappuser','kawaiiapp123','arqui_kawaii')
        # prepare a cursor object using cursor() method
        try:

            with con.cursor() as cur:

                cur.execute('SELECT VERSION()')

                version = cur.fetchone()

                print("Database version: .'version[0]'.")

        finally:

            con.close()

def consultar(sqlquery):
    cur.execute(sqlquery)
    return cur.fetchall()

def modificar(sqlquery):
    cur.execute(sqlquery)
    connect.commit()

def cerrar():
    try:
        cur.close()
        connect.close()
        print("Conexión con base de datos cerrada")
    except:
        print("Error al cerrar conexión")


def llenado(largo):
    aux = str(largo)
    while len(aux) < 5:
        aux = '0' + aux
    print(aux)
    return aux


connection()
