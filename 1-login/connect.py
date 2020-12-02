import psycopg2

global connect
global cur

def connection():
    try:
        connect= None
        cur= None
        connect = psycopg2.connect(host="localhost", database="kawaii_db", user="kawaiiapp", password="kawaii123")
        print("Conexión con base de datos establecida")
        cur = connect.cursor()
    except:
        print("Error de conexión con base de datos")

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
#y = modificar("insert into funcionarios(especialidad, rut, nombre) values ('Enfermero', '196443732', 'cristobal-urrutia')")
#modificar("update funcionarios set rut = '123456789' where nombre = 'cristobal-castro'")
#x = consultar("select * from funcionarios")
#cerrar()
#print(x)
