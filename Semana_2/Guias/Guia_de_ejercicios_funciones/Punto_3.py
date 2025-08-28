def area_triangulo (b:int, a:int)-> float:
    return (b * a) /2

print("VAMOS A CALCULAR EL AREA DE UN TRIANGULO, POR FAVOR COMPLETAR LOS DATOS PEDIDOS PARA REALIZAR EL CALCULO")
print("---------------------------------------------------------------------------------------------------------")

base = int(input("Ingrese el valor de la base del triangulo: "))
altura = int(input("Ingrese el valor de la altura del triangulo: "))

resultado_area = area_triangulo(base, altura)

print(f"El area del triangulo es {resultado_area}")