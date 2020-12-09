import socket  
from conect import *
#query de la consulta de un paciente mediante rut 


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   
s.connect(("localhost", 5000)) 
s.send(bytes('00010sinitcodig','utf-8'))
recibido=s.recv(4096)
print(recibido)

while True:
    datos = s.recv(4096)
    if datos.decode('utf-8').find('codig'):
        datos = datos[10:]
        target = datos.decode()
        target = "'"+target+"'"
        sql = 'select consultas.nombre_paciente, funcionarios.nombre, diagnosticos.diagnostico, diagnosticos.sintomas, diagnosticos.comentarios, diagnosticos.id from diagnosticos, funcionarios, consultas where funcionarios.id = diagnosticos.funcionarios_id and diagnosticos.consultas_id = consultas.id and consultas.rut_paciente = '+target
        respuesta2 = 'codig' + "no_existe_usuario"
        conexion()
        x = consultar(sql)
        cerrar()
        y = ""
        for i in range(0, len(x)):
                for j in range (0, len(x[i])):
                    y += str(x[i][j])+","  
                y = y[:len(y)-1]+";"
        print(y)        
        print(respuesta2)
        temp=llenado(len(respuesta2))  
        print('tmp: ', temp)
        print('tmp + respuesta:',temp+respuesta2)
        if len(y) == 0:
            y = "no hay diagnosticos asociados al rut ingresado"
        s.send(bytes(temp+respuesta2+y,'utf-8'))


        

        #realizar la operacion de buscar en la bd
        
        

        #crear mensaje de respuesta
        print("envia3")
    else:
        pass
    
s.close()