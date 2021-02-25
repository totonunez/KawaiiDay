import socket
from connect import *


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost",5000))
s.send(bytes('00010sinitaddev'))
recibido = s.recv(4096)
print(recibido)

while True:
    datos = s.recv(4096)
    if 'addev' in datos.decode('utf-8'):
        datos = datos[10:]
        target = datos.decode()
        data = target.split()
        consulta = "INSERT INTO evento (lat,lng,nombre)VALUES ('%s','%s','%s');"%(data[0],data[1],data[2])
        respuesta = consultar(consulta)

        if respuesta == ():
            respuesta = "Evento agregado!"
            print(respuesta)
            pass

    else:
        pass
