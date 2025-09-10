enteros = [0] * 10


suma_enteros = 0

for numero in range(len(enteros)):
    enteros[numero] = int(input(f"Ingrese el numero {numero + 1}: "))

for numero in range(len(enteros)):
    suma_enteros += enteros[numero]

print(f"La suma de los datos cargados es igual a {suma_enteros}")