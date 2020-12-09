#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket  

from conect import *


#query de la consulta de un paciente mediante rut 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
s.connect(("localhost",5000)) 
s.send(bytes('00010sinitsupfu','utf8'))
print("enviado \n")
recibido = s.recv(4096)
print(recibido)


# realizar la operacion de creacion de consulta a la base de datos

while True:
    datos = s.recv(4096)
    if datos.decode('utf-8').find('supfu'):
        #decodificar el mensaje
        datos = datos[10:]
        target = datos.decode('utf-8')
        print(target)
        data = target.split()

        #realizar la operacion de buscar en la bd
        
        # especialidad | rut | nombre 
        


        consulta = f"INSERT INTO funcionarios (especialidad, rut, nombre) VALUES ('{data[2]}','{data[1]}','{data[0]}');"

        
        respuesta = modificar(consulta)
        
        if respuesta == None:
            respuesta = "usuario anadido con exito"
        
        
        
        

        respuesta='supfu'+str(respuesta)
        print(respuesta)
        temp=llenado(len(respuesta))  
        print('tmp: ', temp)
        print('tmp + respuesta:',temp+respuesta)
        s.send(bytes(temp+respuesta,'utf-8'))

        
        

        
        

        #crear mensaje de respuesta
        print("envia3")
    else:
        pass
    

s.close()