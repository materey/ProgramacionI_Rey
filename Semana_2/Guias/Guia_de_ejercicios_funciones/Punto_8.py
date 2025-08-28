def calcular_edad (año_nacimineto:int)-> int:
    return 2025 - año_nacimineto

año = int(input("Ingrese su año de nacimiento: "))

edad = calcular_edad(año)

print(f"Tenes {edad} años")
