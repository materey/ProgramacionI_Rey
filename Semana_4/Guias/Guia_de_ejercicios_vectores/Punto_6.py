enteros = [0] * 7


for numero in range(len(enteros)):
    enteros[numero] = int(input(f"Ingrese el elemento {numero + 1}: "))

mayor = enteros[0]
for numero in range(len(enteros)):
    if enteros[numero] > mayor:
        mayor = enteros[numero]
print(f"El numero mayor es {mayor} y se encuentra en la posicion {numero}")
