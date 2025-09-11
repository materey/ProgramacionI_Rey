enteros = [0] * 10

for numero in range(len(enteros)):
    enteros[numero] = int(input(f"Ingrese el elemento {numero + 1}: "))

for numero in range(len(enteros)):
    if enteros[numero] % 2 == 0:
        enteros[numero] = 0

for numero in range(len(enteros)):
    print(enteros[numero])