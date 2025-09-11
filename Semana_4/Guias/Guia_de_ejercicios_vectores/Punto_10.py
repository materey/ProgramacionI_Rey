def buscar_en_array (array, buscado):
    for i in range(len(array)):
        if array[i] == buscado:
            return i + 1
    return -1



array = [0] * 5
for i in range(len(array)):
    array[i] = int(input(f"Ingrese el elemento {i + 1}: "))

buscado = int(input("Ingrese el numero que desea buscar: "))

resultado = buscar_en_array(array, buscado)

if resultado != -1:
    print(f"El numero {buscado} se encontro por primera vez en la posicion {resultado}")
else:
    print(f"El numero {buscado} no se encontro en el array")