import pymysql

con = pymysql.connect('167.86.114.135','arqui_kawaiiappuser','kawaiiapp123','arqui_kawaii')
def connection():

        # prepare a cursor object using cursor() method
        try:

            with con.cursor() as cur:

                cur.execute('SELECT VERSION()')

                version = cur.fetchone()

                print('Database version:')

        finally:

            con.close()

def consultar(sqlquery):
        try:

            with con.cursor() as cur:
                cur.execute(sqlquery)
                return cur.fetchall()
        finally:

            con.close()

def modificar(sqlquery):
    con.cursor().execute(sqlquery)
    #connect.commit()

def cerrar():
    try:
        con.cursor().close()
        connect.close()
        print("Conexion con base de datos cerrada")
    except:
        print("Error al cerrar conexion")


def llenado(largo):
    aux = str(largo)
    while len(aux) < 5:
        aux = '0' + str(aux)
    print(aux)
    return aux


connection()
#y = modificar("insert into funcionarios(especialidad, rut, nombre) values ('Enfermero', '196443732', 'cristobal-urrutia')")
#modificar("update funcionarios set rut = '123456789' where nombre = 'cristobal-castro'")
#x = consultar("select * from funcionarios")
#cerrar()
#print(x)
