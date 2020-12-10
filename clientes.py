import socket
import time
import datetime
from connect import *


especialidad = ["cardiologia", "pediatria", "broncopulmonar", "med_interna", "med_general"]
examenes = ["electroenfelalograma", "pcr", "muestra_de_sangre", "TAC", "glucosa"]
previsiones = ["fonasa", "colmena", "avansalud", "banmedica" , "otro"]
#conexion de socket cliente

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 5000))
s.send(bytes('00005getsv'))
recibido = s.recv(4096)
print("mira papu")
print(recibido)
print("mira papu")

rutAux = ""

while True:
    s.send(bytes('00010getsvlogin'))
    rut = str(raw_input("escriba su rut sin puntos ni guion:"))
    password = str(raw_input("password:"))
    #verificacion de valores
    #construccion del mensaje a enviar
    datos = str(rut) +" "+ str(password)
    temp = llenado(len(str(datos)+'login'))
    mensaje = str(temp) +'login'+ str(datos)
    s.send(bytes(mensaje))
    recibido = s.recv(4096)
    recibido = s.recv(4096)

    print(recibido[15:])

    recibido = recibido[15:].decode()
    if recibido != "not_user":
        rutAux = rut
        break

#interfaz
while True:

    opcion = int(raw_input("""Que servicio desea:
	2.- registrar  evento
	3.- solicitar  consulta por rut de paciente
	4.- registrar funcionario de salud
    5.- consulta de lista de espera
    6.- registrar orden de examen a paciente (pide rut)
    7.- solicitar orden de examen de paciente
    8.- registrar diagnostico de paciente
    9.- solicitar diagnostico de paciente
    0.- salir
	\n"""))

    if(opcion == 2):
        # se debe estar con sesion iniciada de entes , luego mover esto al if de op 1
        print("Ha seleccionado registrar evento")
        s.send(bytes('00010getsvaddev'))
        print("papuuuuu")
        print(s.recv(4096))
        namae = raw_input("Escriba nombre del evento: ")
        fechita = raw_input("escriba fecha  de la consulta (formato: dd/mm/aaaa): ")
        lat = raw_input("ingrese latitud del evento: ")
        lng = raw_input("ingrese longitud del evento: ")

        #verificacion de valores:
        name = namae.replace(" ", "_")
        date = fechita.replace("/","")
        #date = datetime.datetime.strptime(date, '%d%m%Y').strftime('%d-%m-%Y')

        #creacion del mensaje

        datos = str(lat) + " " + str(lng) + " " + str(name)
        temp = llenado(len(datos+'addev'))
        mensaje = str(temp) + 'addev' + str(datos)
        s.send(bytes(mensaje))
        recibido = s.recv(4096)


        print(recibido[14:])

    if(opcion == '3'):
        # se debe estar con sesion iniciada de entes, luego mover esto al if de op 1
        print("Ha seleccionado la opcion: 'solicitar consulta': \n")
        s.send(bytes('00010getsvconpa'))

        datos = raw_input("Escribir rut de paciente ( formato: 11111111): \n")
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
        s.send(bytes('00010getsvsupfu'))


        #ingreso de valores
        nombre = raw_input("escriba su nombre completo separados por espacios: \n ")
        rut = raw_input("escriba su rut (formato: 12345678): ")
        print("escoja El NUMERO de su especialidad: \n")
        for x in range(0,len(especialidad)):
            print(str(x)+ " "+ especialidad[x])

        i = int(raw_input("opcion: "))
        esp = especialidad[i]

        #verificacion de los valores
        name = nombre.replace(" ", "_")


        #envio de mensaje
        datos = name +" "+ rut + " " + esp
        temp = llenado(len(datos+'supfu'))
        mensaje = temp+'supfu'+datos
        s.send(bytes(mensaje))
        recibido = s.recv(4096)

        recibido = s.recv(4096)

        print(recibido[12:])

    if(opcion == "5"):
        # se debe estar con sesion iniciada de entes , luego mover esto al if de op 1
        print("Ha seleccionado 'consultar paciente en lista de espera'")
        s.send(bytes('00010getsvconli'))



        #ingreso de valores

        #verificacion de los valores



        #envio de mensaje

        temp = llenado(len('conli'))
        mensaje = temp + 'conli' + 'consultar_lista'
        print(mensaje)
        s.send(bytes(mensaje))
        recibido = s.recv(4096)
        recibido = s.recv(4096)
        print(recibido[12:])


    if(opcion == "6"):
        # se debe estar con sesion iniciada de entes , luego mover esto al if de op 1
        print("Ha seleccionado 'registrar orden de examen': \n" )
        s.send(bytes('00010getsvaddex'))


        #ingreso de valores
        hora = input("escriba la hora (formato: hh:mm): \n ")
        rut = input("escriba su rut (formato: 12345678): ")
        print("escoja El NUMERO del tipo de examen: \n")
        for x in range(0,len(examenes)):
            print(str(x)+ " "+ examenes[x])

        i = int(input("opcion: "))
        ex = examenes[i]
        #verificacion de los valores



        #envio de mensaje
        datos = hora + " " + rut + " " + ex
        temp = llenado(len(datos+'addex'))
        mensaje = temp + 'addex' + datos
        s.send(bytes(mensaje))
        recibido = s.recv(4096)
        recibido = s.recv(4096)
        print(recibido[12:])






    if(opcion == "7"):
        # se debe estar con sesion iniciada de entes , luego mover esto al if de op 1
        print("Ha seleccionado 'consultar orden de examen': \n")
        s.send(bytes('00010getsvconex','utf-8'))

        #ingreso de valores
        datos = input("Escribir rut de paciente (formato: 11111111): \n")

        #verificacion de los datos


        #creacion del mensaje a enviar
        temp = llenado(len(datos+'conex'))
        mensaje = temp + 'conex' + datos
        s.send(bytes(mensaje))
        recibido = s.recv(4096)
        recibido = s.recv(4096)
        print(recibido[12:])






    if(opcion == "8"):
        # se debe estar con sesion iniciada de entes , luego mover esto al if de op 1
        print("Ha seleccionado 'registrar diagnostico de paciente'")
        s.send(bytes('00010getsvadddi'))

        #ingreso de datos
        sintomas = input("Escribir sintomas  (formato: sintoma1sin-toma2-sintoma3... : )")
        diagnostico = input("Escribir diagnostico: )")
        comentarios = input("Escribir comentarios: )")
        idDiagnostico = input("Id de consulta: )")


        #verificacion de valores (el rut)


        datos = sintomas + ";" + diagnostico + ";" + comentarios + ";" + idDiagnostico + ";" + rutAux
        temp = llenado(len(datos+'adddi'))
        mensaje = temp + 'adddi' + datos
        s.send(bytes(mensaje))
        recibido = s.recv(4096)
        recibido = s.recv(4096)
        print(recibido[29:].decode())




    if(opcion == "9"):
        # se debe estar con sesion iniciada de entes , luego mover esto al if de op 1
        print("Ha seleccionado 'consultar diagnostico de paciente'")
        s.send(bytes('00010getsvcodig'))

        #ingreso de valores
        datos = input("Escribir rut de paciente (formato: 11111111): \n")

        #verificacion de los datos

        #crear mensaje
        temp = llenado(len(datos+'codig'))
        mensaje = temp + 'codig' + datos
        s.send(bytes(mensaje))
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
        s.send(bytes('quit'))
        time.sleep(5)
        break

print("ha cerrado terminal")
#s.close()
