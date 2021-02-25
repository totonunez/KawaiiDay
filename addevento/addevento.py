import socket
from connect import *


#query de la consulta de un paciente mediante rut

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost",5000))
s.send(bytes('00010sinitaddev'))
recibido = s.recv(4096)
print(recibido)

while True:
    datos = s.recv(4096)
    print(datos)
    if datos.decode('utf-8').find('addevento'):
        print(datos)
        datos = datos[10:]
        target = datos.decode()
        print(target)
        data = target.split()
        consulta = "INSERT INTO evento (lat, lng, nombre) VALUES ({},{},{});".format(data[0],data[1],str(data[2]))
        respuesta = modificar(consulta)

        if respuesta == None:
            respuesta = "Evento agregado!"

        print(respuesta)
        temp=llenado(len(respuesta))
        s.send(bytes(temp+respuesta))

    else:
        pass

s.close()
