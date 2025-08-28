def buscar_mayor (a:int, b:int, c:int)-> int:
    if a >= b and a >= c:
        if b >= c:
            return a, b, c
        else:
            return a, c, b
    elif b >= a and b >= c:
        if a >= c:
            return b, a, c
        else:
            return b, c, a
    else:
        if a >= b:
            return c, a, b
        else:
            return c, b, a
        


print("ORDENAR TRES NUMEROS DE MAYOR A MENOR")


numero_1 = int(input("Ingresar el primer numero: "))
numero_2 = int(input("Ingresar el segundo numero: "))
numero_3 = int(input("Ingresar el tercer numero: "))

mayor, medio, menor = buscar_mayor(numero_1, numero_2, numero_3)

print(f"Numeros ordenados {mayor}, {medio}, {menor}")

