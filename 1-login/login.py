import socket  
from conect import *
#query de la consulta de un paciente mediante rut 


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   
s.connect(("localhost", 5000)) 
s.send(bytes('00010sinitlogin','utf-8'))
recibido=s.recv(4096)
print(recibido)

while True:
    datos = s.recv(4096)
    if datos.decode('utf-8').find('login'):
        #decodificar el mensaje
        datos = datos[10:]
        target = datos.decode()
        print(target)
        data = target.split()
        r = []
        n = []


        consulta = f"SELECT  funcionarios.rut, funcionarios.especialidad FROM funcionarios WHERE funcionarios.rut = '{data[0]}' AND funcionarios.especialidad = '{data[1]}'"
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
        s.send(bytes(temp+respuesta2,'utf-8'))


        

        #realizar la operacion de buscar en la bd
        
        

        #crear mensaje de respuesta
        print("envia3")
    else:
        pass
    
s.close()

