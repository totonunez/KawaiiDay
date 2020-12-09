#!/usr/bin/env python
# -*- coding: utf-8 -*-
#servicio de añadir consulta
import socket  
from conect import *


#query de la consulta de un paciente mediante rut 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
s.connect(("localhost",5000)) 
s.send(bytes('00010sinitaddco','utf8'))
recibido = s.recv(4096)
print(recibido)

# realizar la operacion de creacion de consulta a la base de datos

while True:
    datos = s.recv(4096)
    if datos.decode('utf-8').find('addco'):
        #decodificar el mensaje
        datos = datos[10:]
        target = datos.decode()
        print(target)
        data = target.split()



        #realizar la operacion de buscar en la bd
        #hora | fecha | provision | rut_paciente | nombre_paciente 
        consulta = f"INSERT INTO consultas (hora, fecha, provision, rut_paciente,nombre_paciente) VALUES ('{data[3]}','{data[2]}', '{data[4]}','{data[1]}','{data[0]}');"

        #INSERT INTO consultas (hora, fecha, provision, rut_paciente,nombre_paciente) VALUES (valor1, valor2, valor3);

        
        respuesta = modificar(consulta)
        
        if respuesta == None:
            respuesta = "usuario anadido con exito"
        
        respuesta='addco'+respuesta
        print(respuesta)
        temp=llenado(len(respuesta))  
        print('tmp: ', temp)
        print('tmp + respuesta:',temp+respuesta)
        s.send(bytes(temp+respuesta,'utf-8'))

        
        

        #crear mensaje de respuesta
        print("envia3")
    else:
        pass
    #elif datos == 'quit':
    #    print ("adios")
    #    s.shutdown()
    #    for sock in s:
    #        sock.close() 
    #    break

s.close()