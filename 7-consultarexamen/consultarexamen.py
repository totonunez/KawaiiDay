import socket  
import os
import sys
scriptpath = "/home/nico/Escritorio/trabajoarqui/ArquideSistemas/"

# Add the directory containing your module to the Python path (wants absolute paths)
sys.path.append(os.path.abspath(scriptpath))
# Do the import
from conect import *



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
s.connect(("localhost",5000)) 
s.send(bytes('00010sinitconex','utf8'))
print("enviado \n")
recibido = s.recv(4096)
print(recibido)

# realizar la operacion de creacion de consulta a la base de datos

while True:
    datos = s.recv(4096)
    print(datos)
    if datos.decode('utf-8').find('conex'):
        datos = datos[10:]
        target = datos.decode()
        print(target)
        data = target.split()
        data = target.split()
        hr = []
        tp = []


        consulta = f"select examenes.hora, examenes.tipo_examen from examenes,diagnosticos,consultas where  consultas.id= diagnosticos.consultas_id and examenes.diagnosticos_id = diagnosticos.id and consultas.rut_paciente = '{data[0]}';"
        respuesta = consultar(consulta)

        if len(respuesta )!= 0:
            for h,t in respuesta: 
                hr.append(h)
                tp.append(t)


                
            respuesta2='conex'+hr[0]+tp[0]
            
        #si ta
        else:
            respuesta2 = 'conex' + "no_hay_examen_asociado"
        
        print(respuesta2)
        temp=llenado(len(respuesta2))  
        print('tmp: ', temp)
        print('tmp + respuesta:',temp+respuesta2)
        s.send(bytes(temp+respuesta2,'utf-8'))









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