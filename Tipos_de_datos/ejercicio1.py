#Ejercicio 1. Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10) y posteriormente muestre en pantalla cada elemento de la lista junto con su cuadrado y su cubo.
numeros_aleatorios = []
for i in range(1,11):
  import random
  random.randint(1,10)
  numeros_aleatorios.append(random.randint(1,10))
print("Los números aleatorios son", numeros_aleatorios)
cuadrado = [numeros_aleatorios ** 2 for numeros_aleatorios in numeros_aleatorios]
print("El cuadrado de los números aleatorios es", cuadrado)
cubo = [numeros_aleatorios ** 3 for numeros_aleatorios in numeros_aleatorios]
print("El cubo de los números aleatorios es", cubo)