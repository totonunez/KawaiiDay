import socket
from connect import *
import time
import ast

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost",5000))
s.send(bytes('00010sinitassst'))
recibido = s.recv(4096)
print(recibido)
while 1:
    datos = s.recv(4096)
    if 'assst' in datos.decode('utf-8'):
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
            respuestita='assst'+'hay_stands'+str(arraynuevito)
            temp=llenado(len(respuestita))
            #print(bytes(temp+respuestita))
            #recibido=sock.recv(4096)
            s.send(temp+respuestita)
            asignacion = s.recv(4096)
            target=asignacion.decode()
            targeti= target[10:]
            arrayassign = targeti.split()
            #print(arrayassign[0])
            consultarut = "SELECT * FROM usuarios WHERE usuarios.rut = %s;" %(arrayassign[1])
            respuestarut = str(consultar(consultarut))
            if respuestarut != "()":
                respuesta2='assst'+'Existe_Usuario'
                print("Existe_Usuario")
                consulta = "INSERT INTO relacion_users_stands (stand,owner) VALUES ('%s','%s');" %(arrayassign[0],arrayassign[1])
                respuesta = consultar(consulta)
                print("Se asigno el stand")
            else:
                respuesta2 = 'assst' + 'usuario_no_existe'
                print("No se asigno el stand")
            temp=llenado(len(respuesta2))
            print(bytes(temp+respuesta2))
            #recibido=sock.recv(4096)
            s.send(temp+respuesta2)
            pass

        else:
            respuestita='assst'+'no_hay_stands'
            temp=llenado(len(respuestita))
            #print(bytes(temp+respuestita))
            #recibido=sock.recv(4096)
            s.send(temp+respuestita)
        pass

    else:
        pass

#s.close()
