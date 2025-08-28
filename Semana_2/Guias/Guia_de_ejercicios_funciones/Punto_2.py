def operaciones(num_1:int, num_2:int)->int:
    suma = num_1 + num_2
    resta = num_1 - num_2 
    multiplicacion = num_1 * num_2
    return suma, resta, multiplicacion


numero_1 = int(input("Numero 1: "))
numero_2 = int(input("Numero 2: "))

resultado_suma, resultado_resta, resultado_multiplicacion = operaciones(numero_1, numero_2)
print(f"El resultado de la suma es {resultado_suma}, el de la resta es {resultado_resta}, y el de la multiplicacion es {resultado_multiplicacion}")
