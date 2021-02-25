import socket
from connect import *

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost",5000))
s.send(bytes('00010sinitaddus'))
recibido = s.recv(4096)
print(recibido)
while 1:
    datos = s.recv(4096)
    if 'addus' in datos.decode('utf-8'):
        datos = datos[10:]
        target = datos.decode()
        data = target.split()
        consulta = "INSERT INTO usuarios (rut,pass)VALUES('%s','%s');"%(data[0],data[1])
        respuesta = consultar(consulta)

        if respuesta == None:
            respuesta = "Usuario Agregado!"
            print(respuesta)
            pass

    else:
        pass
