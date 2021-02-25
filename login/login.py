import socket
from connect import *


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost", 5000))
sock.send(bytes('00010sinitlogin'))
recibido=sock.recv(4096)
print(recibido)

while True:
    datos = sock.recv(4096)
    if datos.decode('utf-8').find('login'):
        #decodificar el mensaje
        datos = datos[10:]
        target = datos.decode()
        print(target)
        data = target.split()
        r = []
        n = []

        consulta = "SELECT * FROM usuarios WHERE usuarios.rut = {} AND usuarios.pass = {}".format(data[0],data[1])
        respuesta = consultar(consulta)
        print(respuesta)
        if len(respuesta)!= 0:
            for rut in respuesta:
                r.append(rut)
            respuesta2='login'+str(r[0])
        else:
                respuesta2 = "Usuario_no_existe"

        print(respuesta2)
        temp=llenado(len(respuesta2))
        sock.send(bytes(temp+respuesta2))
    else:
        pass

s.close()
