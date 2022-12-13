def numero_par(numero):
    if numero % 2 == 0:
        par = True
        print("El numero es par")
    else:
        par = False
        print("El numero es impar")
    return par
#Construir un programa que reciba 5 numeros y los almacene en una lista solo si el numero dado es par
lista_pares = []
for i in range(5):
    numero = int(input())
    n_par = numero_par(numero)
    print(n_par)
    if n_par:
        lista_pares.append(numero)
print(lista_pares[::-1])
