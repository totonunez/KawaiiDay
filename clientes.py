import socket
import time
import datetime
from conect import *


especialidad = ["cardiologia", "pediatria", "broncopulmonar", "med_interna", "med_general"]
examenes = ["electroenfelalograma", "pcr", "muestra_de_sangre", "TAC", "glucosa"]
previsiones = ["fonasa", "colmena", "avansalud", "banmedica" , "otro"]
#conexion de socket cliente

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 5000))
s.send(bytes('00005getsv','utf-8'))
recibido = s.recv(4096)

rutAux = ""

while True:
    opcion = input("""Que servicio desea: 
	1.- iniciar sesión funcionario 
    0.- salir
	\n""")

    if(opcion == "1"):
        print("Ha seleccionado la opcion 'iniciar sesión de funcionario '")
        s.send(bytes('00010getsvlogin','utf-8'))

        #singreso de valores
        rut = input("escriba su rut (formato: 12345678): ")
        print("escoja El NUMERO de su especialidad: \n")
        for x in range(0,len(especialidad)):
            print(str(x) + " " + especialidad[x])
        i = int(input("opcion: "))
        esp = especialidad[i]

        #verificacion de valores

        #construcción del mensaje a enviar
        datos = rut + " "+ esp 
        temp = llenado(len(datos+'login'))
        mensaje = temp +'login'+ datos
        s.send(bytes(mensaje,'utf-8'))
        recibido = s.recv(4096)
        recibido = s.recv(4096)
        print(recibido[12:])
        recibido = recibido[12:].decode()
        if recibido != "no_existe_usuario":
            rutAux = rut
            break
    if opcion == "0":
        break

#interfaz
while True:
    if opcion == "0":
        s.send(bytes('quit','utf-8'))
        time.sleep(5)
        break

    opcion = input("""Que servicio desea: 
	2.- registrar  consulta
	3.- solicitar  consulta por rut de paciente
	4.- registrar funcionario de salud
    5.- consulta de lista de espera
    6.- registrar orden de examen a paciente (pide rut)
    7.- solicitar orden de examen de paciente
    8.- registrar diagnostico de paciente
    9.- solicitar diagnostico de paciente
    0.- salir
	\n""")
    
    if(opcion == '2'):
        # se debe estar con sesión iniciada de entes , luego mover esto al if de op 1
        print("Ha seleccionado 'registrar consulta'")
        s.send(bytes('00010getsvaddco','utf-8'))


        #ingresar dato

        nombre = input("escriba su nombre completo separados por espacios: \n ")


        rut = input("escriba su rut (formato: 11111111): \n ")

        fecha = input("escriba fecha  de la consulta (formato: dd/mm/aaaa): \n ")

        hora = input("escriba hora de la consulta (formato: hh:mm): \n ")

        print("escoja El NUMERO de su prevision de salud: \n")
        for x in range(0,len(previsiones)):
            print(str(x)+ " "+ previsiones[x])

        i = int(input("opcion: "))
        prev = previsiones[i]

        




        #verificacion de valores:
        name = nombre.replace(" ", "_")
        date = fecha.replace("/","-")
        date = datetime.datetime.strptime(date, '%d-%m-%Y').strftime('%Y-%m-%d')
        

        

        #creacion del mensaje

        datos = name + " " + rut + " " + date + " " + hora + " " + prev
        temp = llenado(len(datos+'addco'))
        mensaje = temp + 'addco' + datos
        s.send(bytes(mensaje,'utf-8'))
        recibido = s.recv(4096)
        recibido = s.recv(4096)
        
        print(recibido[12:])

    if(opcion == '3'):
        # se debe estar con sesión iniciada de entes, luego mover esto al if de op 1
        print("Ha seleccionado la opcion: 'solicitar consulta': \n")
        s.send(bytes('00010getsvconpa','utf-8'))
        
        #ingreso de dato

        datos = input("Escribir rut de paciente ( formato: 11111111): \n")
        # verificacion del dato


        #enviar mensaje
        aux = llenado(len(datos+'conpa'))
        mensaje = aux + 'conpa' + datos
        s.send(mensaje.encode())
        recibido = s.recv(4096)
       
        recibido = s.recv(4096)
       
        print(recibido[12:])

    if(opcion =="4"):
        print("Ha seleccionado 'registrar funcionario':  \n")
        s.send(bytes('00010getsvsupfu','utf-8'))
        
        
        #ingreso de valores
        nombre = input("escriba su nombre completo separados por espacios: \n ")
        rut = input("escriba su rut (formato: 12345678): ")
        print("escoja El NUMERO de su especialidad: \n")
        for x in range(0,len(especialidad)):
            print(str(x)+ " "+ especialidad[x])

        i = int(input("opcion: "))
        esp = especialidad[i]

        #verificación de los valores
        name = nombre.replace(" ", "_")
        

        #envio de mensaje
        datos = name +" "+ rut + " " + esp
        temp = llenado(len(datos+'supfu'))
        mensaje = temp+'supfu'+datos
        s.send(bytes(mensaje,'utf-8'))
        recibido = s.recv(4096)
        
        recibido = s.recv(4096)
        
        print(recibido[12:])

    if(opcion == "5"):
        # se debe estar con sesión iniciada de entes , luego mover esto al if de op 1
        print("Ha seleccionado 'consultar paciente en lista de espera'")
        s.send(bytes('00010getsvconli','utf-8'))
        


        #ingreso de valores
        
        #verificación de los valores



        #envio de mensaje
        
        temp = llenado(len('conli'))
        mensaje = temp + 'conli' + 'consultar_lista'
        print(mensaje)
        s.send(bytes(mensaje,'utf-8'))
        recibido = s.recv(4096)
        recibido = s.recv(4096)
        print(recibido[12:])


    if(opcion == "6"):
        # se debe estar con sesión iniciada de entes , luego mover esto al if de op 1
        print("Ha seleccionado 'registrar orden de examen': \n" )
        s.send(bytes('00010getsvaddex','utf-8'))


        #ingreso de valores
        hora = input("escriba la hora (formato: hh:mm): \n ")
        rut = input("escriba su rut (formato: 12345678): ")
        print("escoja El NUMERO del tipo de examen: \n")
        for x in range(0,len(examenes)):
            print(str(x)+ " "+ examenes[x])

        i = int(input("opcion: "))
        ex = examenes[i]
        #verificación de los valores



        #envio de mensaje
        datos = hora + " " + rut + " " + ex
        temp = llenado(len(datos+'addex'))
        mensaje = temp + 'addex' + datos
        s.send(bytes(mensaje,'utf-8'))
        recibido = s.recv(4096)
        recibido = s.recv(4096)
        print(recibido[12:])
        





    if(opcion == "7"):
        # se debe estar con sesión iniciada de entes , luego mover esto al if de op 1
        print("Ha seleccionado 'consultar orden de examen': \n")
        s.send(bytes('00010getsvconex','utf-8'))
        
        #ingreso de valores
        datos = input("Escribir rut de paciente (formato: 11111111): \n")

        #verificacion de los datos


        #creacion del mensaje a enviar
        temp = llenado(len(datos+'conex'))
        mensaje = temp + 'conex' + datos
        s.send(bytes(mensaje,'utf-8'))
        recibido = s.recv(4096)
        recibido = s.recv(4096)
        print(recibido[12:])






    if(opcion == "8"):
        # se debe estar con sesión iniciada de entes , luego mover esto al if de op 1
        print("Ha seleccionado 'registrar diagnostico de paciente'")
        s.send(bytes('00010getsvadddi','utf-8'))

        #ingreso de datos
        sintomas = input("Escribir sintomas  (formato: sintoma1sin-toma2-sintoma3... : )")
        diagnostico = input("Escribir diagnostico: )")
        comentarios = input("Escribir comentarios: )")
        idDiagnostico = input("Id de consulta: )")


        #verificacion de valores (el rut)
         

        datos = sintomas + ";" + diagnostico + ";" + comentarios + ";" + idDiagnostico + ";" + rutAux
        temp = llenado(len(datos+'adddi'))
        mensaje = temp + 'adddi' + datos
        s.send(bytes(mensaje,'utf-8'))
        recibido = s.recv(4096)
        recibido = s.recv(4096)
        print(recibido[29:].decode())




    if(opcion == "9"):
        # se debe estar con sesión iniciada de entes , luego mover esto al if de op 1
        print("Ha seleccionado 'consultar diagnostico de paciente'")
        s.send(bytes('00010getsvcodig','utf-8'))
        
        #ingreso de valores
        datos = input("Escribir rut de paciente (formato: 11111111): \n")

        #verificacion de los datos

        #crear mensaje
        temp = llenado(len(datos+'codig'))
        mensaje = temp + 'codig' + datos
        s.send(bytes(mensaje,'utf-8'))
        recibido = s.recv(4096)
        recibido = s.recv(4096)
        recibido = recibido[29:].decode()
        cont = 0
        text = ""
        print("Respuesta:", recibido)
        if recibido != "no hay diagnosticos asociados al rut ingresado":
            for i in range(0,len(recibido)):
                if recibido[i] != "," and recibido[i] != ";":
                    text += recibido[i]
                elif cont == 0:
                    print("Nombre paciente: ", text)
                    text = ""
                    cont += 1
                elif cont == 1:
                    print("Nombre funcionario: ", text)
                    text = ""
                    cont += 1
                elif cont == 2:
                    print("Diagnostico: ", text)
                    text = ""
                    cont += 1   
                elif cont == 3:
                    print("Sintomas: ", text)
                    text = ""
                    cont += 1    
                elif cont == 4:
                    print("Comentarios: ", text)
                    text = ""
                    cont += 1           
                elif cont == 5:
                    print("Numero de diagnostico: ", text)
                    text = ""
                    cont = 0  
                    print("--o--")                               
        else:
            print(recibido)

    if(opcion == "0"):
        s.send(bytes('quit','utf-8'))
        time.sleep(5)
        break

print("ha cerrado terminal")
s.close()
