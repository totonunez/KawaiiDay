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


        consulta = "SELECT  funcionarios.rut, funcionarios.especialidad FROM funcionarios WHERE funcionarios.rut = '{data[0]}' AND funcionarios.especialidad = '{data[1]}'"
        respuesta = consultar(consulta)
        print(respuesta)

        #si el usuario no esta

        if len(respuesta )!= 0:
            for rut,nombre in respuesta:
                r.append(rut)
                n.append(nombre)
            respuesta2='login'+r[0]+n[0]

        #si ta
        else:
            respuesta2 = 'login' + "no_existe_usuario"

        print(respuesta2)
        temp=llenado(len(respuesta2))
        print('tmp: ', temp)
        print('tmp + respuesta:',temp+respuesta2)
        sock.send(bytes(temp+respuesta2))




        #realizar la operacion de buscar en la bd



        #crear mensaje de respuesta
        print("envia3")
    else:
        pass

s.close()
