enteros = [0] * 8

mayores_de_100 = 0

for i in range(len(enteros)):
    enteros[i] = int(input(f"Ingrese el numero {i + 1}: "))
    if enteros[i] > 100:
        mayores_de_100 += 1

print(f"La cantidad de numeros mayores a 100 es {mayores_de_100}")
