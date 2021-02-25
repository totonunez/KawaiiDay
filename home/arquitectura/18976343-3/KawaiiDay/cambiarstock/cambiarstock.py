import socket
from connect import *
import time
import ast

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost",5000))
s.send(bytes('00010sinitchstk'))
recibido = s.recv(4096)
print(recibido)
while 1:
    datos = s.recv(4096)
    if 'chstk' in datos.decode('utf-8'):
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
            respuestita='chstk'+'hay_stands'+str(arraynuevito)
            temp=llenado(len(respuestita))
            #print(bytes(temp+respuestita))
            #recibido=sock.recv(4096)
            s.send(temp+respuestita)
            asignacion = s.recv(4096)
            target=asignacion.decode()
            targeti= target[10:]
            arrayassign = targeti.split()
            #print(arrayassign[0])
            consulta = "SELECT producto FROM relacion_productos_stands WHERE stand = '%s';" %(arrayassign[0])
            respuesta = consultar(consulta)
            arraynuevito2 = []
            for y in respuesta:
                arraynuevito2.append(y[0])
            if respuesta!= ():
                respuestita='chstk'+'hay_produc'+str(arraynuevito2)
                temp=llenado(len(respuestita))
                s.send(temp+respuestita)
                stock = s.recv(4096)
                target=stock.decode()
                targeti= target[10:]
                arrayassign = targeti.split()
                consulta = "UPDATE relacion_productos_stands SET cantidad='%s' WHERE producto = '%s';" %(arrayassign[0],arrayassign[1])
                respuesta = consultar(consulta)
                if respuesta != ():
                    print("Stock Actualizado!")
                else:
                    respuestita='chstk'+'no_hay_produc'
                    temp=llenado(len(respuestita))
                    #print(bytes(temp+respuestita))
                    #recibido=sock.recv(4096)
                    s.send(temp+respuestita)
                pass
        else:
            respuestita='chstk'+'no_hay_stands'
            temp=llenado(len(respuestita))
            #print(bytes(temp+respuestita))
            #recibido=sock.recv(4096)
            s.send(temp+respuestita)
        pass

    else:
        pass

#s.close()
