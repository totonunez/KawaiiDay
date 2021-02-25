import socket
from connect import *
import time
import ast

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost",5000))
s.send(bytes('00010sinitasspr'))
recibido = s.recv(4096)
print(recibido)
while 1:
    datos = s.recv(4096)
    if 'asspr' in datos.decode('utf-8'):
        datos = datos[10:]
        target = datos.decode()
        data = target.split()
        consulta = "SELECT nombre FROM stands;"
        respuesta = consultar(consulta)
        arraynuevito = []
        for x in respuesta:
            arraynuevito.append(x[0])

        if respuesta != ():
            #print(arraynuevito)
            respuestita='asspr'+'hay_stands'+str(arraynuevito)
            temp=llenado(len(respuestita))
            #print(bytes(temp+respuestita))
            #recibido=sock.recv(4096)
            s.send(temp+respuestita)
            asignacion = s.recv(4096)
            target=asignacion.decode()
            targeti= target[10:]
            arrayassign = targeti.split()
            consulta = "INSERT INTO relacion_productos_stands (stand,producto) VALUES ('%s','%s');" %(arrayassign[0],arrayassign[1])
            respuesta = consultar(consulta)
            if respuesta != ():
                print("Producto Agregado!")

        else:
            respuestita='asspr'+'no_hay_stands'
            temp=llenado(len(respuestita))
            #print(bytes(temp+respuestita))
            #recibido=sock.recv(4096)
            s.send(temp+respuestita)
        pass

    else:
        pass

#s.close()
