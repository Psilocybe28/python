#creamos un diccionario vacio con nombre "compra"
compra = {}
#Pedimos al usuario ingresar el nombre y precio del primer producto
nombre1 = input("Ingresa el producto a comprar ")
precio1 = int(input("Ingresa el precio "))
nombre2 = input("Ingresa el producto a comprar ")
precio2 = int(input("Ingresa el precio "))
#usamos la funccion "int" para camiar a entero el numero ingresado por el usuario
#ya que la funcion inputo regresa valores string
# agregamos el nombre1 y orecio1 al diccionario
compra[nombre1] = precio1
compra[nombre2] = precio2
#Se crea una lina de 80 caracteres usando el signo = pra representar una linea
print("=" * 80)
#El encabezado se coloca al centro utilizando el signo ^ 
encabezado = f'{"producto":^20}{"Precio":^20}'
fila1 = f'{nombre1:^20}{compra[nombre1]}'
fila2 = f'{nombre2:^20}{compra[nombre2]}'
print(encabezado)
print(fila1)
print(fila2)