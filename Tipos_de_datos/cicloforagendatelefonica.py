# Pedir al usuario el nombre y numero del contacto para agregar a la agenda
N = int(input("Cantidad de contactos "))
contactos = {}
for i in range(N):
    nombre = input("Nombre ")
    numero = int(input("Numero "))
    #agregar la clave-nombre y el valor-numero al diccionario
    contactos[nombre] = numero
    print(contactos)