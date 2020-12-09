import socket  

from conect import *






s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
s.connect(("localhost",5000)) 
s.send(bytes('00010sinitconli','utf8'))
print("enviado \n")
recibido = s.recv(4096)
print(recibido)

# realizar la operacion de creacion de consulta a la base de datos

while True:
    datos = s.recv(4096)
    print(datos)
    if datos.decode('utf-8').find('conli'):
        #decodificar el mensaje
        datos = datos[10:]
        target = datos.decode()
        print(target)
        data = target.split()
        hr = []
        date = []
        prov = []
        rut = []
        name = []





        consulta = f"select * from consultas where consultas.id not in (select consultas.id from consultas, diagnosticos where consultas.id = diagnosticos.consultas_id);"
        respuesta = consultar(consulta)

        for ids,hora,fecha,provision,r,n in respuesta:
            hr.append(hora)
            date.append(fecha)
            prov.append(provision)
            rut.append(r)
            name.append(n)

        res = ""

        print(hr)
        print(date)
        print(prov)
        print(rut)
        print(name)

        for i in range(0,len(hr)):
            res = str(hr[i]) + " " + str(date[i])+ " " +str(prov[i]) +" "+ str(rut[i]) + " " + str(name[i])+ " "

        


        respuesta = 'conli' + res


        
        print(respuesta)
        temp=llenado(len(respuesta))  
        print('tmp: ', temp)
        print('tmp + respuesta:',temp+respuesta)
        s.send(bytes(temp+respuesta,'utf-8'))




        #realizar la operacion de buscar en la bd
        
        

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