print("pilares")
nombre = input("Ingresa el nombre de un producto")
precio = float(input("Ingresa el precio de un producto"))
cantidad = int(input("Cantidad de productos"))
subtotal = precio * cantidad
encabezado = f'{"producto":<15}{"precio":<15}{"cantidad":<15}{"subtotal":<15}'
print(encabezado)
fila1 = f'{nombre:<15}{precio:<15}{cantidad:<15}{subtotal:<15}\n'
fila2 = f'{nombre:<15}{precio:<15}{cantidad:<15}{subtotal:<15}\n'
fila3 = f'{nombre:<15}{precio:<15}{cantidad:<15}{subtotal:<15}\n'
datos = fila1 + fila2 + fila3
print(datos)

