enteros = [0] * 10

for i in range(len(enteros)):
    enteros[i] = int(input(f"Ingrese el elemento {i + 1}: "))


numero_buscado = int(input("Ingrese el numero a buscar: "))

encontrado = False
for i in range(len(enteros)):
    if enteros[i] == numero_buscado:
        print(f"El numero {numero_buscado} se encuentra en la posicion {i + 1}")
        encontrado = True
        break

if not encontrado:
    print(f"El numero {numero_buscado} no esta en el array")



