def es_par (n:int)-> int:
    if n % 2 == 0:
        return True
    else:
        return False




numero = int(input("Ingrese un numero: "))

if es_par(numero):
    print(f"El numero {numero} es par")
else:
    print(f"El numero {numero} es impar")