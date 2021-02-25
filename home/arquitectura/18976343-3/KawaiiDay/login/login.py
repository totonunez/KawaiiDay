import socket
from connect import *
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost", 5000))
sock.send("00000sinitlogon")
recibido=sock.recv(4096)
print(recibido)

while 1:
    print("esperando conexion")
    datos = sock.recv(4096)
    if 'logon' in datos.decode('utf-8'):
        #decodificar el mensaje
        datos = datos[10:]
        #target = datos.decode()
        data = datos.split()
        r = []
        consulta = "SELECT * FROM usuarios WHERE usuarios.rut = %s AND usuarios.pass = %s" %(data[0],data[1])
        respuesta = str(consultar(consulta))
        print(respuesta)
        if respuesta != "()":
            for rut in respuesta:
                r.append(rut)
            respuesta2='logon'+'Existe_Usuario'
            print("Existe_Usuario")

        else:
            respuesta2 = 'logon' + 'usuario_no_existe'

        temp=llenado(len(respuesta2))
        print(bytes(temp+respuesta2))
        #recibido=sock.recv(4096)
        time.sleep(2)
        sock.send(temp+respuesta2)
        pass

    else:
        pass
