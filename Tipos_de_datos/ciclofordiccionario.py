# Pedir al usuario el numero de productos a comprar
N = int(input("Numero de productos "))
compra = {}
for i in range(N):
    nombre = input("Producto ")
    precio = float(input("Precio "))
    #agregar la clave, nombre y el valor precio al diccionario
    compra[nombre] = precio
    print(compra)
