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
s.send(bytes('00010sinitadddi','utf8'))
print("enviado \n")
recibido = s.recv(4096)
print(recibido)



# realizar la operacion de creacion de consulta a la base de datos

while True:
    datos = s.recv(4096)
    x = datos.decode()
    if datos.decode('utf-8').find('adddi'):
        datos = datos[10:]
        target = datos.decode()
        print(target)
        arr = []
        x = ""
        targetAux = target+';'
        print(targetAux)
        for i in range(0, len(targetAux)):
            if targetAux[i] != ';':
                x += targetAux[i]
            else:
                arr.append(x)
                x = ""        
        print("bla bla: ", arr)
        comentarios = "'"+arr[2]+"'"
        diagnostico = "'"+arr[1]+"'"
        sintomas = "'"+arr[0]+"'"
        funcionario = "'"+arr[4]+"'"
        consulta = arr[3]
        sql = 'select funcionarios.id from funcionarios where funcionarios.rut = '+funcionario
        conexion()
        idFuncionario = consultar(sql)
        idFuncionario = str(idFuncionario[0][0])
        cerrar()
        sql = 'insert into diagnosticos(comentarios, diagnostico, sintomas, funcionarios_id, consultas_id) values ('+comentarios+','+diagnostico+','+sintomas+','+idFuncionario+','+consulta+')'
        conexion()
        modificar(sql)
        cerrar()
        respuesta2 = 'adddi' + "no_existe_usuario"
        temp=llenado(len(respuesta2))  
        print('tmp: ', temp)
        print('tmp + respuesta:',temp+respuesta2)
        y = 'El diagnostico se registro correctamente'
        s.send(bytes(temp+respuesta2+y,'utf-8'))

    else:
        pass
    #elif datos == 'quit':
    #    print ("adios")
    #    s.shutdown()
    #    for sock in s:
    #        sock.close() 
    #    break

s.close()