import socket
import time
import datetime
from connect import *
import ast
from termcolor import colored

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 5000))
s.send(bytes('00005getsv'))
recibido = s.recv(4096)
print(recibido)

rutsiti = ""

while 1:
    opcioningreso = int(raw_input("Ingresar [0]\nSeleccionar opcion (solo numero):"))
    if(opcioningreso == 0):
        print(colored("Ha seleccionado Ingresar al sistema\n","yellow"))
        s.send(bytes('00010getsvlogon'))
        datos = s.recv(4096)
        rut = str(raw_input("escriba su rut sin puntos ni guion:"))
        password = str(raw_input("password:"))
        datos = str(rut) +" "+ str(password)
        temp = llenado(len(str(datos)+'logon'))
        mensaje = str(temp) + 'logon' + str(datos)
        s.send(bytes(mensaje))
        datosi = s.recv(4096)
        if 'usuario_no_existe' in datosi.decode('utf-8'):
            print("Acceso denegado")
            target = datos.decode()
            pass
        else:
            if 'Existe_Usuario' in datosi.decode('utf-8'):
                break
            #data = datos.split()
            #print(data)
        #recibido = recibido.decode()
        #print(recibido)

#interfaz
while 1:

    opcion = int(raw_input("Que servicio desea:\n2.- registrar  evento\n3.- crear stand\n4.-asignar Stand\n5.-Crear usuario\n6.-Crear Producto\n7.-Asignar Producto a Stand\n8.-cambiar Stock de producto\nSeleccionar opcion (Solo numero): "))

    if(opcion == 2):
        print(colored("Ha seleccionado Registrar evento\n","yellow"))
        s.send(bytes('00010getsvaddev'))
        #print("papuuuuu")
        #print(s.recv(4096))
        namae = raw_input("Escriba nombre del evento: ")
        fechita = raw_input("escriba fecha  de la consulta (formato: dd/mm/aaaa): ")
        lat = raw_input("ingrese latitud del evento: ")
        lng = raw_input("ingrese longitud del evento: ")

        #verificacion de valores:
        name = namae.replace(" ","_")
        date = fechita.replace("/","")
        #date = datetime.datetime.strptime(date, '%d%m%Y').strftime('%d-%m-%Y')
        datos = str(lat) + " " + str(lng) + " " + str(name)
        temp = llenado(len(datos+'addev'))
        mensaje = str(temp) + 'addev' + str(datos)
        s.send(bytes(mensaje))
        pass
    if(opcion == 3):
        print(colored("Ha seleccionado Registrar Stand\n","yellow"))
        s.send(bytes('00010getsvaddst'))
        #print("papuuuuu")
        #print(s.recv(4096))
        namae = raw_input("Escriba nombre del stand: ")
        name = namae.replace(" ","_")
        datos = str(name)
        temp = llenado(len(datos+'addst'))
        mensaje = str(temp) + 'addst' + str(datos)
        s.send(bytes(mensaje))
        pass

    if(opcion ==4):
        print(colored("Ha seleccionado Asignar stand a usuario\n","yellow"))
        s.send(bytes('00010getsvassst'))
        #print("papuuuuu")
        print(s.recv(4096))
        temp = llenado(len("fffff"+'assst'))
        mensaje = str(temp) + 'assst' + str("fffff")
        s.send(bytes(mensaje))
        datosi = s.recv(4096)
        if 'hay_stands' in datosi.encode('ascii'):
            print("hay stands")
            target = datosi.decode()
            datosisi = target[22:]
            datosisi2 = ast.literal_eval(datosisi)
            print("El nombre de los stands que hay son:\n")
            for y in datosisi2:
                print(y)
            print("\n")
            namaeseleccion = str(raw_input("Cual es el stand que selecciona?(escriba su nombre):"))
            rutseleccion = str(raw_input("Cual es el rut que desea asignar?(escriba su rut sin puntos ni guion):"))
            name = namaeseleccion.replace(" ","_")
            datos = str(name) + " " + str(rutseleccion)
            temp = llenado(len(datos+'assst'))
            mensaje = str(temp) + 'assst' + str(datos)
            s.send(bytes(mensaje))
            datosi = s.recv(4096)
            if 'usuario_no_existe' in datosi.decode('utf-8'):
                print("No existe el usuario")
                target = datos.decode()
                pass
            else:
                if 'Existe_Usuario' in datosi.decode('utf-8'):
                    print("Usuario Existe")
                    pass
        else:
            if 'no_hay_stands' in datosi.decode('utf-8'):
                print("no hay stands")
                pass
        pass
    if(opcion == 5):
        print(colored("Ha seleccionado Agregar Usuario\n","yellow"))
        s.send(bytes('00010getsvaddus'))
        print(s.recv(4096))
        rutsito = str(raw_input("Escriba su rut sin puntos ni guion "))
        passwi = str(raw_input("Escriba su password, solo numeros: "))
        datos = rutsito+" "+passwi
        temp = llenado(len(str(datos)+'addus'))
        mensaje = str(temp) + 'addus' + str(datos)
        #print(mensaje[10:])
        s.send(bytes(mensaje))
        pass

    if(opcion == 6):
        print(colored("Ha seleccionado Registrar Producto\n","yellow"))
        s.send(bytes('00010getsvaddpr'))
        #print("papuuuuu")
        #print(s.recv(4096))
        namae = raw_input("Escriba nombre del producto: ")
        precio = raw_input("Escriba precio del producto: ")
        name = namae.replace(" ","_")
        datos = str(name) + " " + str(precio)
        temp = llenado(len(datos+'addpr'))
        mensaje = str(temp) + 'addpr' + str(datos)
        s.send(bytes(mensaje))
        pass

    if(opcion ==7):
        print(colored("Ha seleccionado Asignar producto Stand\n","yellow"))
        s.send(bytes('00010getsvasspr'))
        #print("papuuuuu")
        print(s.recv(4096))
        temp = llenado(len("fffff"+'asspr'))
        mensaje = str(temp) + 'asspr' + str("fffff")
        s.send(bytes(mensaje))
        datosi = s.recv(4096)
        if 'hay_stands' in datosi.encode('ascii'):
            print("hay stands")
            target = datosi.decode()
            datosisi = target[22:]
            datosisi2 = ast.literal_eval(datosisi)
            print("El nombre de los stands que hay son:\n")
            for y in datosisi2:
                print(y)
            print("\n")
            namaeseleccion = str(raw_input("Cual es el stand que selecciona?(escriba su nombre):"))
            productoseleccion = str(raw_input("Cual es el producto que desea asignar?(escriba el nombre del producto):"))
            name = namaeseleccion.replace(" ","_")
            datos = str(name) + " " + str(productoseleccion)
            temp = llenado(len(datos+'asspr'))
            mensaje = str(temp) + 'asspr' + str(datos)
            s.send(bytes(mensaje))
        else:
            if 'no_hay_stands' in datosi.decode('utf-8'):
                print("no hay stands")
                pass
        pass

    if(opcion ==8):
        print(colored("Ha seleccionado Cambiar Stock\n","yellow"))
        s.send(bytes('00010getsvchstk'))
        #print("papuuuuu")
        print(s.recv(4096))
        temp = llenado(len("fffff"+'chstk'))
        mensaje = str(temp) + 'chstk' + str("fffff")
        s.send(bytes(mensaje))
        datosi = s.recv(4096)
        if 'hay_stands' in datosi.encode('ascii'):
            print("hay stands")
            target = datosi.decode()
            datosisi = target[22:]
            datosisi2 = ast.literal_eval(datosisi)
            print("El nombre de los stands que hay son:\n")
            for y in datosisi2:
                print(y)
            print("\n")
            namaeseleccion = str(raw_input("Cual es el stand que selecciona?(escriba su nombre):"))
            name = namaeseleccion.replace(" ","_")
            datos = str(name)
            temp = llenado(len(datos+'chstk'))
            mensaje = str(temp) + 'chstk' + str(datos)
            s.send(bytes(mensaje))
            datosi = s.recv(4096)
            if 'hay_produc' in datosi.encode('ascii'):
                print("hay productos")
                target = datosi.decode()
                datosisi = target[22:]
                datosisi2 = ast.literal_eval(datosisi)
                print("El nombre de los productos que hay son:\n")
                for y in datosisi2:
                    print(y)
                print("\n")
                namaeseleccion = str(raw_input("Cual es el producto que selecciona?(escriba su nombre):"))
                cantidad = str(raw_input("Cual es el nuevo stock en el producto?(escriba su nombre):"))
                name = namaeseleccion.replace(" ","_")
                datos = str(cantidad) + " " + str(name)
                temp = llenado(len(datos+'chstk'))
                mensaje = str(temp) + 'chstk' + str(datos)
                s.send(bytes(mensaje))

            else:
                if 'no_hay_produc' in datosi.decode('utf-8'):
                    print("no hay productos")
                    pass
        else:
            if 'no_hay_stands' in datosi.decode('utf-8'):
                print("no hay stands")
                pass
        pass
print("ha cerrado terminal")
#s.close()
