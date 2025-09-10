enteros = [0] * 6

for i in range(len(enteros)):
    enteros[i] = int(input(f"Ingrese el elemento {i + 1}: "))


for i in range(5, -1, -1):
    print(enteros[i])
